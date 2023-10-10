from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from .forms import TerrorFormulario, CienciaficcionFormulario, FantasiaFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class ListaCienciaFiccion(ListView):

    model = CienciaFiccion

class DetalleCienciaFiccion(DetailView):

    model = CienciaFiccion

class CrearCienciaFiccion(CreateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]

class ActualizarCienciaFiccion(UpdateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]

class BorrarCienciaFiccion(DeleteView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["libro", "autor", "year"]
           


