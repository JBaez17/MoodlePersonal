from django.db import models

class Alumno(models.Model):

    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    nombre = models.CharField(max_length = 65)
    apellidos = models.CharField('Apellidos',max_length = 120)
    mail = models.EmailField('E-mail', max_length=60)

    def __str__(self):
        return self.nombre
