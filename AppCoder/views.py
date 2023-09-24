from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
from AppCoder.models import *


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def curso(request):

    return render(request, "AppCoder/cursos.html")


def servicio(request):
    
    return render(request, "AppCoder/servicios.html")

def carrera(request):
    
    return render(request, "AppCoder/carreras.html")

def cursoFormulario(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Cursos(curso=info["curso"], modalidad=info["modalidad"], correo=info["correo"]) 

            curso.save()

            return render(request, "AppCoder/inicio.html")
        
    else: 

        formulario1 = CursoFormulario()    


    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})



def busquedaCurso(request):

    return render(request, "AppCoder/inicio.html")


def resultados(request):

    if request.GET["curso"]:

        curso=request.GET["curso"]
        cursos = Cursos.objects.filter(curso__icontains=curso)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "curso":curso})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)



def servicioFormulario(request):

    pass

   

