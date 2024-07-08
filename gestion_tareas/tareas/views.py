# tareas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm
from rest_framework import viewsets
from .serializers import ProyectoSerializer, TareaSerializer
import logging

crud_logger = logging.getLogger('crud_logger')

def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'tareas/index.html', {'proyectos': proyectos})

def proyecto_detalle(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'tareas/proyecto_detalle.html', {'proyecto': proyecto, 'tareas': tareas})

def tarea_detalle(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    return render(request, 'tareas/tarea_detalle.html', {'tarea': tarea})

def proyecto_nuevo(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save()
            crud_logger.debug(f"Proyecto creado: {proyecto.nombre}")
            return redirect('proyecto_detalle', id=proyecto.id)
    else:
        form = ProyectoForm()
    return render(request, 'tareas/proyecto_nuevo.html', {'form': form})

def tarea_nueva(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            crud_logger.debug(f"Tarea creada: {tarea.nombre}")
            return redirect('tarea_detalle', id=tarea.id)
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_nueva.html', {'form': form, 'proyecto': proyecto})

def proyecto_editar(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save()
            crud_logger.debug(f"Proyecto editado: {proyecto.nombre}")
            return redirect('proyecto_detalle', id=proyecto.id)
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'tareas/proyecto_editar.html', {'form': form, 'proyecto': proyecto})

def tarea_editar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save()
            crud_logger.debug(f"Tarea editada: {tarea.nombre}")
            return redirect('tarea_detalle', id=tarea.id)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/tarea_editar.html', {'form': form, 'tarea': tarea})

def proyecto_borrar(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    crud_logger.debug(f"Proyecto borrado: {proyecto.nombre}")
    return redirect('index')

def tarea_borrar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    proyecto_id = tarea.proyecto.id
    tarea.delete()
    crud_logger.debug(f"Tarea borrada: {tarea.nombre}")
    return redirect('proyecto_detalle', id=proyecto_id)

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
