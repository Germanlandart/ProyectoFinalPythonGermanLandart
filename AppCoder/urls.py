from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("",inicio, name="Inicio"),
    path("cienciaficcion/<int:pk>", DetalleCienciaFiccion.as_view(), name="CienciaFiccionDetalle"),
    path("cienciaficcion/list/", ListaCienciaFiccion.as_view(), name="CienciaFiccionLeer"),
    path("cienciaficcion/crear/", CrearCienciaFiccion.as_view(), name="CienciaFiccionCrear"),
    path("cienciaficcion/editar/<int:pk>", ActualizarCienciaFiccion.as_view(), name="CienciaFiccionActualizar"),
    path("cienciaficcion/borrar/<int:pk>", BorrarCienciaFiccion.as_view(), name="CienciaFiccionBorrar"),
    path("terror/<int:pk>", DetalleTerror.as_view(), name="TerrorDetalle"),
    path("terror/list/", ListaTerror.as_view(), name="TerrorLeer"),
    path("terror/crear/", CrearTerror.as_view(), name="TerrorCrear"),
    path("terror/editar/<int:pk>", ActualizarTerror.as_view(), name="TerrorActualizar"),
    path("terror/borrar/<int:pk>", BorrarTerror.as_view(), name="TerrorBorrar"),
    path("fantasia/<int:pk>", DetalleFantasia.as_view(), name="FantasiaDetalle"),
    path("fantasia/list/", ListaFantasia.as_view(), name="FantasiaLeer"),
    path("fantasia/crear/", CrearFantasia.as_view(), name="FantasiaCrear"),
    path("fantasia/editar/<int:pk>", ActualizarFantasia.as_view(), name="FantasiaActualizar"),
    path("fantasia/borrar/<int:pk>", BorrarFantasia.as_view(), name="FantasiaBorrar"),
    path("login/", InicioSesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),

    ]

