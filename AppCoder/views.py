from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def InicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Datos incorrectos"})
    else:

        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario":form})    

             



def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado."})
        
    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario":form})           

@login_required
def editarUsuario(request):

    usuario = request.user
    
    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")
        
    else: 

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })    

    return  render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})   



def inicio(request):
    return render(request, "AppCoder/inicio.html")


def busquedaterror(request):

    return render(request, "AppCoder/inicio.html")

@login_required
def resultados(request):

    if request.GET["terror"]:

        terror=request.GET["terror"]
        terror = terror.objects.filter(terror__icontains=terror)

        return render(request, "AppCoder/inicio.html", {"terror":terror})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


@login_required
def agregarAvatar(request):

    if request.method =="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render(request,"AppCoder/agregarAvatar.html", {"formulario":form})        



class ListaCienciaFiccion(LoginRequiredMixin, ListView):

    model = CienciaFiccion

class DetalleCienciaFiccion(LoginRequiredMixin, DetailView):

    model = CienciaFiccion

class CrearCienciaFiccion(LoginRequiredMixin, CreateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]

class ActualizarCienciaFiccion(LoginRequiredMixin, UpdateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]

class BorrarCienciaFiccion(LoginRequiredMixin, DeleteView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]


class ListaFantasia(LoginRequiredMixin, ListView):

    model = Fantasia

class DetalleFantasia(LoginRequiredMixin, DetailView):

    model = Fantasia

class CrearFantasia(LoginRequiredMixin, CreateView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["libro", "autor", "year"]

class ActualizarFantasia(LoginRequiredMixin, UpdateView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["libro", "autor", "year"]

class BorrarFantasia(LoginRequiredMixin, DeleteView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["libro", "autor", "year"]
           

class ListaTerror(LoginRequiredMixin, ListView):

    model = Terror

class DetalleTerror(LoginRequiredMixin, DetailView):

    model = Terror

class CrearTerror(LoginRequiredMixin, CreateView):

    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["libro", "autor", "year"]

class ActualizarTerror(LoginRequiredMixin, UpdateView):

    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["libro", "autor", "year"]

class BorrarTerror(LoginRequiredMixin, DeleteView):

    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["libro", "autor", "year"]
