from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_terminacion']
        widgets = {
            'fecha_terminacion': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'type': 'datetime-local'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('Este campo es obligatorio.')
        if len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_fecha_terminacion(self):
        fecha_terminacion = self.cleaned_data.get('fecha_terminacion')
        if fecha_terminacion and fecha_terminacion < timezone.now():
            raise ValidationError('La fecha de terminación no puede ser en el pasado.')
        return fecha_terminacion

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_terminacion']
        widgets = {
            'fecha_terminacion': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'type': 'datetime-local'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('Este campo es obligatorio.')
        if len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_fecha_terminacion(self):
        fecha_terminacion = self.cleaned_data.get('fecha_terminacion')
        if fecha_terminacion and fecha_terminacion < timezone.now():
            raise ValidationError('La fecha de terminación no puede ser en el pasado.')
        return fecha_terminacion
