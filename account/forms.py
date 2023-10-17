from django import forms
from .models import UserModel, addresses


class CustomRegisterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}), label="Ad")
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}), label="Soyad")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}), label="Kullanıcı Adı")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="E-posta")
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Adres")
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Telefon Numarası")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Parola")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Parola Tekrar")
    
    class Meta:
        model = UserModel
        fields = ("name", "surname", "username", "email", "address", "phone_number", "password1", "password2")


class CustomLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Kullanıcı Adı")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Parola")

    class Meta:
        model = UserModel
        fields = ("username", "password")


class createAdminForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, required=True)
    email = forms.EmailField(widget=forms.EmailInput, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class adminLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"username"}), required=True, label='Kullanıcı adı:')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "id":"password1"}), required=True, label='Parola:')

    class Meta:
        model = UserModel
        fields = ('username','password1')


class profilePhotoForm(forms.ModelForm):
    profile_photo = forms.ImageField(widget=forms.FileInput(attrs={"class":"profile_photo_input"}))
    class Meta:
        model = UserModel
        fields = ('profile_photo', )


class addressForm(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={"id":"city"}),label='Şehir' )
    county = forms.CharField(widget=forms.TextInput(attrs={"id":"county"}),label='İlçe')
    district = forms.CharField(widget=forms.TextInput(attrs={"id":"district"}),label='Mahalle')
    street = forms.CharField(widget=forms.TextInput(attrs={"id":"street"}),label='Sokak')
    number = forms.CharField(widget=forms.TextInput(attrs={"id":"number"}),label='No')
    class Meta:
        model = addresses
        fields = ('city', 'county', 'district', 'street', 'number',)

