from dataclasses import fields
from django import forms 
from .models import Profile

from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserFormAuth(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


# class RegisterUserForm(UserCreationForm):
#     username = forms.CharField(label="Имя", widget=forms.TextInput())
#     password1 =forms.CharField(label = "Пароль", widget=forms.PasswordInput())
#     password2 = forms.CharField(label="Повторите пароль", widget = forms.PasswordInput())

#     class Meta:
#         model = get_user_model()
#         fields = ["username"]



class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label = "Имя", widget = forms.TextInput())
    password1 = forms.CharField(label = "Пароль", widget = forms.PasswordInput())
    password2 = forms.CharField(label = "Повторите пароль", widget = forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]


    def clean_paaword(self):
        passw = self.cleaned_data
        if passw["password1"] !=  passw["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return passw["password1"]
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username = username).exists():
            raise forms.ValidationError("Пользователь с данным именем уже существует")
        return username
    


class ProfileUser(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile', "bio"]