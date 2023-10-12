from django.db import models
from django.contrib.auth.models import User 

class Terror(models.Model):
    
    libro = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    year = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to= "imagenes" )
    descripcion = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        return f"Libro: {self.libro} ------ Autor: {self.autor} ------ Year: {self.year}"
    
class Comentario(models.Model):
    comentario = models.ForeignKey(Terror, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    
class ComentarioCF(models.Model):
    comentario = models.ForeignKey(Terror, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)    

class ComentarioF(models.Model):
    comentario = models.ForeignKey(Terror, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)    
        

class CienciaFiccion(models.Model):

    def __str__(self):

        return f"Libro: {self.libro} ------ Autor: {self.autor} ------ Year: {self.year}"

    libro = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    year = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to= "imagenes" )
    descripcion = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

       
class Fantasia(models.Model):

    def __str__(self):

        return f"Libro: {self.libro} ------ Autor: {self.autor} ------ Year: {self.year}"

    libro = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    year = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to= "imagenes" )
    descripcion = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)



