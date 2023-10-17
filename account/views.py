from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import CustomRegisterForm, CustomLoginForm, createAdminForm, adminLoginForm, profilePhotoForm, addressForm
from .models import UserModel, addresses

def user_login(request):
    if request.method == "POST":
        username1 = request.POST["username"]
        password1 = request.POST["password"]

        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            login(request, user)
            return redirect("homePage")
        else:
            form = CustomLoginForm
            return render(request, "account/login.html", {"error":"Kullanıcı adı yada parola hatalı !", "form":form})

    else:
        form = CustomLoginForm
    return render(request, 'account/login.html', {"form":form})

def register(request):
    if request.method == "POST":
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        address = request.POST["address"]
        phone_number = request.POST["phone_number"]

        if password1 == password2:        
            if UserModel.objects.filter(username=username).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"Kullanıcı adı başkası tarafından kullanılıyor !",
                                                                 "form":form,
                                                                 "email":email,
                                                                 "adres":address,
                                                                 "phone_number":phone_number})
            
            elif not str(first_name).isalpha() or not str(last_name).isalpha():
                form = CustomRegisterForm()
                return render(request, "account/register.html", {"error":"Ad veya soyad bölümünde harften başka karakter kullanılamaz !",
                                                                 "form":form,
                                                                 "name":first_name,
                                                                 "surname":last_name,
                                                                 "username":username,
                                                                 "email":email,
                                                                 "adres":address,
                                                                 "phone_number":phone_number})
            
            elif UserModel.objects.filter(email=email).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"E-posta sistemde kayıtlı !",
                                                                 "form":form,
                                                                 "name":first_name,
                                                                 "surname":last_name,
                                                                 "username":username,
                                                                 "adres":address,
                                                                 "phone_number":phone_number
                                                                })
            
            elif UserModel.objects.filter(address__exact=''):
                form = CustomRegisterForm
                user = UserModel.objects.create_user(name=first_name, surname=last_name, username=username, email=email, password=password1, address=address, phone_number=phone_number,)
                user.save()
                return redirect("login")
              
            elif UserModel.objects.filter(address=address).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"Adres sistemde kayıtlı !",
                                                                "form":form,
                                                                "name":first_name,
                                                                "surname":last_name,
                                                                "email":email,
                                                                "username":username,
                                                                "phone_number":phone_number})
            
            elif UserModel.objects.filter(phone_number=phone_number).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"Telefon numarası sistemde kayıtlı !",
                                                                 "form":form,
                                                                 "name":first_name,
                                                                 "surname":last_name,
                                                                 "email":email,
                                                                 "adres":address,
                                                                 "username":username})
            
            elif UserModel.objects.filter(phone_number__exact=''):
                form = CustomRegisterForm
                user = UserModel.objects.create_user(name=first_name, surname=last_name, username=username, email=email, password=password1, address=address, phone_number=phone_number,)
                user.save()
                return redirect("login")
                        
            else:
                user = UserModel.objects.create_user(name=first_name, surname=last_name, username=username, email=email, password=password1, address=address, phone_number=phone_number,)
                user.save()
                return redirect("login")
            
        else:
            form = CustomRegisterForm
            return render(request, "account/register.html", {"error":"Şifreler uyuşmuyor !",
                                                             "form":form,
                                                             "name":first_name,
                                                             "surname":last_name,
                                                             "username":username,
                                                             "email":email,
                                                             "adres":address,
                                                             "phone_number":phone_number})
        
    else:
        form = CustomRegisterForm
    return render(request, 'account/register.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('homePage')



def adminregister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if UserModel.objects.filter(username=username).exists():
                form = createAdminForm()
                return render(request, "account/createAdmin.html", {'error':'Kullanıcı adı sistemde mevcut !',
                                                                    'form':form,
                                                                    'email':email,})
            else:
                if UserModel.objects.filter(email=email).exists():
                    form = createAdminForm()
                    return render(request, "account/createAdmin.html", {'error':'Email sistemde mevcut !',
                                                                        'form':form,
                                                                        'username':username,})
                else:
                    user = UserModel.objects.create_superuser(username=username, email=email, password=password1)
                    user.is_staff = False
                    user.save()

                    return redirect("adminLogin")

        else:
            form = createAdminForm()
            return render(request, "account/createAdmin.html", {'error':'Şifreler birbiriyle uyuşmuyor !','form':form})

    else:
        form = createAdminForm()
    return render(request, "account/createAdmin.html", {'form':form})

def adminlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("homePage")

        else:
            form = adminLoginForm()
            return render(request, "account/loginAdmin.html", {'error':'Kullanıcı adı yada parola yanlış !', 'form':form})

    else:
        form = adminLoginForm()
    return render(request, "account/loginAdmin.html", {'form':form})


def profile(request):
    if request.method == 'POST':
        thisUser = UserModel.objects.get(id=request.user.id)
        item = profilePhotoForm(request.POST, request.FILES, instance=thisUser)
        if item.is_valid():
            item.save()
            return redirect("profile")    
    
    else:
        form = profilePhotoForm()
        adres_form = addressForm()
        address = addresses.objects.filter(userAddress=request.user).order_by("-date")
    return render(request, "account/profile.html", {'form':form, "address":address, "addressForm":adres_form,})



def change_address(request):
    address = addresses.objects.filter(userAddress=request.user)
    if request.method == 'POST':
        adres = request.POST.get('adres')
        if adres:
            request.user.address = adres
            request.user.save()
            return redirect('profile')
        else:
            return render(request, "account/profile.html", {"error":"Bir adres seçmelisiniz !", "address":address})
    return redirect('profile')



def addAddress(request):
    if request.method == "POST":
        adres_form = addressForm(request.POST)
        user = UserModel.objects.get(id=request.user.id)
        if adres_form.is_valid():
            thisUser = adres_form.save(commit=False)
            thisUser.userAddress = user
            thisUser.save()

            return redirect('profile')
        

def delete_address(request,id):
    adres = addresses.objects.get(id=id)
    if request.method == "POST":
        adres.delete()
        return redirect('profile')
        