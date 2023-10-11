from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class TerrorFormulario(forms.Form):

    libro = forms.CharField()
    autor = forms.CharField()
    year = forms.IntegerField()


class CienciaficcionFormulario(forms.Form):

    libro = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=60)
    year = forms.IntegerField()

class FantasiaFormulario(forms.Form):

    libro = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=60)
    year = forms.IntegerField()


class UsuarioRegistro(UserCreationForm): 

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User   
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]



class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User   
        fields = ["email", "first_name", "last_name", "password1", "password2"]




class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]