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



def inicio(request):
    return render(request, "AppCoder/inicio.html")

def terror(request):

    return render(request, "AppCoder/terror.html")


def cienciaficcion(request):
    
    return render(request, "AppCoder/cienciaficcion.html")

def fantasia(request):
    
    return render(request, "AppCoder/fantasia.html")

def crearTerror(request):

    if request.method == "POST":

        formulario1 = TerrorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            terror = Terror(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            terror.save()

            return render(request, "AppCoder/terror.html")
        
    else: 

        formulario1 = TerrorFormulario()    


        return render(request, "AppCoder/crearTerror.html", {"form1":formulario1})



def busquedaterror(request):

    return render(request, "AppCoder/inicio.html")


def resultados(request):

    if request.GET["terror"]:

        terror=request.GET["terror"]
        terror = terror.objects.filter(terror__icontains=terror)

        return render(request, "AppCoder/inicio.html", {"terror":terror})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)



def crearCienciaFiccion(request):

    if request.method == "POST":

        formulario1 = CienciaficcionFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            cienciaficcion = CienciaFiccion(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            cienciaficcion.save()

            return render(request, "AppCoder/cienciaficcion.html")
        
    else: 

        formulario1 = CienciaficcionFormulario()    


    return render(request, "AppCoder/crearCienciaFiccion.html", {"form1":formulario1})


def crearFantasia(request):

    if request.method == "POST":

        formulario1 = FantasiaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            fantasia = Fantasia(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            fantasia.save()

            return render(request, "AppCoder/fantasia.html")
        
    else: 

        formulario1 = FantasiaFormulario()    


    return render(request, "AppCoder/crearFantasia.html", {"form1":formulario1})


def leerCienciaFiccion(request):

    cienciaficcion = CienciaFiccion.objects.all()

    contexto = {"cienciaf": cienciaficcion}
    
    return render(request, "AppCoder/leerCienciaFiccion.html", contexto)


def eliminarCienciaFiccion(request, nombreLibro):

    cienciaficcion = CienciaFiccion.objects.get(libro=nombreLibro)
    cienciaficcion.delete()

    libros = CienciaFiccion.objects.all()

    contexto = {"cienciaf":libros}

    return render(request, "AppCoder/leerCienciaFiccion.html", contexto)



def editarCienciaFiccion (request, nombreLibro):

    cienciaficcion = CienciaFiccion.objects.get(libro=nombreLibro)
    
    if  request.method == "POST":

        formulario1 = CienciaficcionFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            cienciaficcion.libro = info["libro"]
            cienciaficcion.autor = info["autor"]
            cienciaficcion.year = info["year"]

            cienciaficcion.save()

            return render(request, "AppCoder/cienciaficcion.html")
        
    else: 

        formulario1 = CienciaficcionFormulario(initial={"nombre":cienciaficcion.libro, "autor":cienciaficcion.autor, 
                                                        "year":cienciaficcion.year})  
          


    return render(request, "AppCoder/editarCienciaFiccion.html", {"form1":formulario1, "libro":nombreLibro})


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
