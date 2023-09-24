from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    modalidad = forms.CharField()
    correo = forms.EmailField()


class ServicioFormulario(forms.Form):

    nombre_servicio = forms.CharField(max_length=60)
    forma_de_pago = forms.CharField(max_length=60)
    correo = forms.EmailField()