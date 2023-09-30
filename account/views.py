from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import CustomRegisterForm, CustomLoginForm, createAdminForm, adminLoginForm
from .models import UserModel

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
        adres = request.POST["address"]
        phone_number = request.POST["phone_number"]

        if password1 == password2:        
            if UserModel.objects.filter(username=username).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"Kullanıcı adı başkası tarafından kullanılıyor !",
                                                                 "form":form,
                                                                 "name":first_name,
                                                                 "surname":last_name,
                                                                 "email":email,
                                                                 "adres":adres,
                                                                 "phone_number":phone_number})
            
            elif UserModel.objects.filter(email=email).exists():
                form = CustomRegisterForm
                return render(request, "account/register.html", {"error":"E-posta sistemde kayıtlı !",
                                                                 "form":form,
                                                                 "name":first_name,
                                                                 "surname":last_name,
                                                                 "username":username,
                                                                 "adres":adres,
                                                                 "phone_number":phone_number
                                                                })
            
            elif UserModel.objects.filter(address=adres).exists():
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
                                                                 "adres":adres,
                                                                 "username":username})
            else:
                user = UserModel.objects.create_user(name=first_name, surname=last_name, username=username, email=email, password=password1, address=adres, phone_number=phone_number,)
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
                                                             "adres":adres,
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
    