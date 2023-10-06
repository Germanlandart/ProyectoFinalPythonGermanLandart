from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("terror/", terror, name="terror"),
    path("cienciaficcion/", cienciaficcion, name="CienciaFiccion"),
    path("fantasia/", fantasia, name="Fantasia"),
    path("terrorFormulario/", terrorFormulario, name="Formularioterror"),
    path("buscarLibro/", busquedaterror, name="Buscarlibro"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("cienciaficcionFormulario/", cienciaficcionFormulario, name="FormularioCienciaFiccion"),
    path("fantasiaFormulario/", fantasiaFormulario, name="Formulariofantasia"),

    #CRUD de cienciaficcion
    path("leerCienciaFiccion/", leerCienciaFiccion, name="CienciaFiccionLeer"),
    
]
