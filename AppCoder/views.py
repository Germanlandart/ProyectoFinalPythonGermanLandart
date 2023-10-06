from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from .forms import TerrorFormulario, CienciaficcionFormulario, FantasiaFormulario


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def terror(request):

    return render(request, "AppCoder/terror.html")


def cienciaficcion(request):
    
    return render(request, "AppCoder/cienciaficcion.html")

def fantasia(request):
    
    return render(request, "AppCoder/fantasia.html")

def terrorFormulario(request):

    if request.method == "POST":

        formulario1 = TerrorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            terror = Terror(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            terror.save()

            return render(request, "AppCoder/terror.html")
        
    else: 

        formulario1 = TerrorFormulario()    


        return render(request, "AppCoder/terrorFormulario.html", {"form1":formulario1})



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



def cienciaficcionFormulario(request):

    if request.method == "POST":

        formulario1 = CienciaficcionFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            cienciaficcion = CienciaFiccion(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            cienciaficcion.save()

            return render(request, "AppCoder/cienciaficcion.html")
        
    else: 

        formulario1 = CienciaficcionFormulario()    


    return render(request, "AppCoder/cienciaficcionFormulario.html", {"form1":formulario1})


def fantasiaFormulario(request):

    if request.method == "POST":

        formulario1 = FantasiaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            fantasia = Fantasia(libro=info["libro"], autor=info["autor"], year=info["year"]) 

            fantasia.save()

            return render(request, "AppCoder/fantasia.html")
        
    else: 

        formulario1 = FantasiaFormulario()    


    return render(request, "AppCoder/fantasiaFormulario.html", {"form1":formulario1})


def leerCienciaFiccion(request):

    cienciaficcion = CienciaFiccion.objects.all()

    contexto = {"cienciaf": cienciaficcion}
    
    return render(request, "AppCoder/leerCienciaFiccion.html", contexto)


def eliminarCienciaFiccion(request):

    cienciaficcion = CienciaFiccion.objects.get
    pass


