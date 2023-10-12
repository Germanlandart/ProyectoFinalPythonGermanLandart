from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import *


class TerrorFormulario(forms.ModelForm):
    class Meta:
        model = Terror
        fields = ('libro', 'autor', 'year', 'imagen', 'descripcion', 'usuario')

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        
class FormularioComentarioF(forms.ModelForm):
    class Meta:
        model = ComentarioF
        fields = ('nombre', 'mensaje')       

class FormularioComentarioCF(forms.ModelForm):
    class Meta:
        model = ComentarioCF
        fields = ('nombre', 'mensaje')              

class CienciaficcionFormulario(forms.ModelForm):

    class Meta:
        model = CienciaFiccion
        fields = ('libro', 'autor', 'year', 'imagen', 'descripcion', 'usuario')


class FantasiaFormulario(forms.ModelForm):

    class Meta:
        model = Fantasia
        fields = ('libro', 'autor', 'year', 'imagen', 'descripcion', 'usuario')

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




