from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    modalidad = forms.CharField()
    correo = forms.EmailField()


class ServicioFormulario(forms.Form):

    nombre_servicio = forms.CharField(max_length=60)
    forma_de_pago = forms.CharField(max_length=60)
    correo = forms.EmailField()

class CarreraFormulario(forms.Form):

    nombre_carrera = forms.CharField(max_length=60)
    nombre_interesado = forms.CharField(max_length=60)
    correo = forms.EmailField()
 
        