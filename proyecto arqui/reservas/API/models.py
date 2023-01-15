from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100, validators=[RegexValidator(r'^(\d{1,3}(?:.\d{1,3}){2}-[\dkK])$', message='Enter a valid rut.')])
    carrera = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    class Meta:
        db_table= "estudiantes"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100, validators=[RegexValidator(r'^(\d{1,3}(?:.\d{1,3}){2}-[\dkK])$', message='Enter a valid rut.')])
    correo = models.EmailField(max_length=100)
    class Meta:
        db_table= "profesores"

class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    class Meta:
        db_table= "espacios"

class Reserva(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL,null=True)
    espacio = models.ForeignKey(Espacio, on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table= "reservas"

