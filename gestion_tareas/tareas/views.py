# tareas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

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
            return redirect('proyecto_detalle', id=proyecto.id)
    else:
        form = ProyectoForm()
    return render(request, 'tareas/proyecto_editar.html', {'form': form})

def tarea_nueva(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
            return redirect('tarea_detalle', id=tarea.id)
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_editar.html', {'form': form})

def proyecto_editar(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save()
            return redirect('proyecto_detalle', id=proyecto.id)
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'tareas/proyecto_editar.html', {'form': form})

def tarea_editar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save()
            return redirect('tarea_detalle', id=tarea.id)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/tarea_editar.html', {'form': form})

def proyecto_borrar(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('index')

def tarea_borrar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('index')
