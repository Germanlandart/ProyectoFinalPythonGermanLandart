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

                return render(request, "AppCoder/inicio2.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

                return render(request, "AppCoder/inicio2.html", {"mensaje":f"Datos incorrectos"})
    else:

        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario":form})    

             



def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio2.html", {"mensaje":"Usuario creado."})
        
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

            return render(request, "AppCoder/inicio2.html", {"mensaje":"Usuario editado correctamente."})
        
    else: 

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })    

    return  render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})   



def inicio(request):
    return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado."})

def about(request):  
    return render(request, "AppCoder/aboutme.html")










@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = request.user

            usuarioActual.avatar_set.all().delete()

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()

            return render(request, "AppCoder/inicio2.html")

    else:
        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario": form})



class ListaCienciaFiccion(LoginRequiredMixin, ListView):

    model = CienciaFiccion

class DetalleCienciaFiccion(LoginRequiredMixin, DetailView):

    model = CienciaFiccion

class CrearCienciaFiccion(LoginRequiredMixin, CreateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class ActualizarCienciaFiccion(LoginRequiredMixin, UpdateView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class BorrarCienciaFiccion(LoginRequiredMixin, DeleteView):

    model = CienciaFiccion
    success_url = "/AppCoder/cienciaficcion/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]


class ListaFantasia(LoginRequiredMixin, ListView):

    model = Fantasia

class DetalleFantasia(LoginRequiredMixin, DetailView):

    model = Fantasia

class CrearFantasia(LoginRequiredMixin, CreateView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class ActualizarFantasia(LoginRequiredMixin, UpdateView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class BorrarFantasia(LoginRequiredMixin, DeleteView):

    model = Fantasia
    success_url = "/AppCoder/fantasia/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]
           

class ListaTerror(LoginRequiredMixin, ListView):

    model = Terror

class DetalleTerror(LoginRequiredMixin, DetailView):

    model = Terror

class CrearTerror(LoginRequiredMixin, CreateView):
    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class ActualizarTerror(LoginRequiredMixin, UpdateView):

    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class BorrarTerror(LoginRequiredMixin, DeleteView):

    model = Terror
    success_url = "/AppCoder/terror/list"   
    fields = ["usuario","libro", "autor", "year", "imagen", "descripcion"]

class Comentario(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = '/comentario.html'
    success_url = "/AppCoder/terror/list"

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(Comentario, self).form_valid(form)
    
class ComentarioCF(LoginRequiredMixin, CreateView):
    model = ComentarioCF
    form_class = FormularioComentarioCF
    template_name = '/comentariocf.html'
    success_url = "/AppCoder/cienciaficcion/list"

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioCF, self).form_valid(form)
    

class ComentarioF(LoginRequiredMixin, CreateView):
    model = ComentarioF
    form_class = FormularioComentarioF
    template_name = '/comentariof.html'
    success_url = "/AppCoder/fantasia/list"

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioF, self).form_valid(form)    