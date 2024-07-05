from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_terminacion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['proyecto', 'nombre', 'descripcion', 'fecha_terminacion']
