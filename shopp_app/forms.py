from django import forms
from .models import shopping_model

class productAddForm(forms.ModelForm):
    class Meta:
        model = shopping_model
        fields = ('title', 'content', 'price', 'image')

    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control input"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control input"}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={"class":"form-control input"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control input"}))

