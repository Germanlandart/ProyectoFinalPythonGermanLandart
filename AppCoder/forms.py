from django import forms

class TerrorFormulario(forms.Form):

    libros = forms.CharField()
    autor = forms.CharField()
    year = forms.IntegerField()


class CienciaficcionFormulario(forms.Form):

    libros = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=60)
    year = forms.IntegerField()

class FantasiaFormulario(forms.Form):

    libros = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=60)
    year = forms.IntegerField()
 
        