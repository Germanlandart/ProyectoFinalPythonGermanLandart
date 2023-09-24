from django.db import models

class Cursos(models.Model):
    
    curso = models.CharField(max_length=60)
    modalidad = models.CharField(max_length=60)
    correo = models.EmailField()

class Servicio(models.Model):

    nombre_servicio = models.CharField(max_length=60)
    forma_de_pago = models.CharField(max_length=60)
    correo = models.EmailField()

       
class Carreras(models.Model):

    nombre_carrera = models.CharField(max_length=60)
    nombre_interesado = models.CharField(max_length=60)
    correo = models.EmailField()
        
