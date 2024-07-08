from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_terminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if self.fecha_terminacion and self.fecha_creacion:
            if self.fecha_terminacion < self.fecha_creacion:
                raise ValidationError('La fecha de terminación no puede ser anterior a la fecha de creación.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Llama a clean() antes de guardar
        super().save(*args, **kwargs)


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_terminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if self.fecha_terminacion and self.fecha_creacion and self.proyecto.fecha_terminacion:
            if self.fecha_terminacion < self.fecha_creacion:
                raise ValidationError('La fecha de terminación no puede ser anterior a la fecha de creación.')
            if self.fecha_terminacion > self.proyecto.fecha_terminacion:
                raise ValidationError('La fecha de terminación de la tarea no puede ser posterior a la fecha de terminación del proyecto.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Llama a clean() antes de guardar
        super().save(*args, **kwargs)
