from django.urls import path
from django import views
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from AppCoder import views


urlpatterns = [
    path("",inicio, name="Inicio"),
    path("cienciaficcion/<int:pk>", DetalleCienciaFiccion.as_view(), name="CienciaFiccionDetalle"),
    path("cienciaficcion/list/", ListaCienciaFiccion.as_view(), name="CienciaFiccionLeer"),
    path("cienciaficcion/crear/", CrearCienciaFiccion.as_view(), name="CienciaFiccionCrear"),
    path("cienciaficcion/editar/<int:pk>", ActualizarCienciaFiccion.as_view(), name="CienciaFiccionActualizar"),
    path("cienciaficcion/borrar/<int:pk>", BorrarCienciaFiccion.as_view(), name="CienciaFiccionBorrar"),
    path("terror/book/<int:pk>", DetalleTerror.as_view(), name="TerrorDetalle"),
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
    path("terror/book/<int:pk>/comentario", Comentario.as_view(template_name="AppCoder/comentario.html"), name='ComentarioTerror'),
    path("fantasia/book/<int:pk>/comentariof", ComentarioF.as_view(template_name="AppCoder/comentariof.html"), name='ComentarioFantasia'),
    path("cienciaficcion/book/<int:pk>/comentariocf", ComentarioCF.as_view(template_name="AppCoder/comentariocf.html"), name='ComentarioCienciaFiccion'),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),
    path("aboutme/", about , name="About"),
    

    
    
    
    ]

