from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("cursos/", curso, name="Cursos"),
    path("servicios/", servicio, name="Servicios"),
    path("carreras/", carrera,name="Carreras"),
    path("cursoFormulario/", cursoFormulario, name="FormularioCurso"),
    path("buscarCurso/", busquedaCurso, name="BuscarCurso"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("servicioFormulario/", servicioFormulario, name="FormularioServicio"),
    path("carreraFormulario/", carrerasFormulario, name="FormularioCarrera"),
    
]
