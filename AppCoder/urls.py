from django.urls import path
from AppCoder.views import *



urlpatterns = [
    path("",inicio, name="Inicio"),
    path("terror/", terror, name="terror"),
    path("cienciaficcion/", cienciaficcion, name="CienciaFiccion"),
    path("fantasia/", fantasia, name="Fantasia"),
    path("crearTerror/", crearTerror, name="TerrorCrear"),
    path("buscarLibro/", busquedaterror, name="Buscarlibro"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("crearFantasia/", crearFantasia, name="FantasiaCrear"),
    path("leerCienciaFiccion/", leerCienciaFiccion, name="CienciaFiccionLee"),
    path("eliminarCienciaFiccion/<nombreLibro>/", eliminarCienciaFiccion, name="CienciaFiccionEliminar"),
    path("editarCienciaFiccion/<nombreLibro>/", editarCienciaFiccion, name="CienciaFiccionEditar"),
    path("cienciaficcion/<int:pk>", DetalleCienciaFiccion.as_view(), name="CienciaFiccionDetalle"),
    path("cienciaficcion/list/", ListaCienciaFiccion.as_view(), name="CienciaFiccionLeer"),
    path("cienciaficcion/crear/", CrearCienciaFiccion.as_view(), name="CienciaFiccionCrear"),
    path("cienciaficcion/editar/<int:pk>", ActualizarCienciaFiccion.as_view(), name="CienciaFiccionActualizar"),
    path("cienciaficcion/borrar/<int:pk>", BorrarCienciaFiccion.as_view(), name="CienciaFiccionBorrar")
    ]

