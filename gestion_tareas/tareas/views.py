# tareas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm
from rest_framework import viewsets
from .serializers import ProyectoSerializer, TareaSerializer
import logging

crud_logger = logging.getLogger('crud_logger')

def inicio(request):
    try:
        return render(request, 'tareas/inicio.html')
    except Exception as e:
        return render(request, 'tareas/error.html', {'message': 'Error al cargar pagina de inicio'})

def index(request):
    try:
        proyectos = Proyecto.objects.all()
        crud_logger.debug(f"Proyectos cargados: {proyectos}")
        return render(request, 'tareas/index.html', {'proyectos': proyectos})
    except Exception as e:
        crud_logger.error(f"Error al cargar los proyectos: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al cargar los proyectos'})

def proyecto_detalle(request, id):
    try:
        proyecto = get_object_or_404(Proyecto, id=id)
        tareas = Tarea.objects.filter(proyecto=proyecto)
        crud_logger.debug(f"Proyecto cargado: {proyecto.nombre}")
        return render(request, 'tareas/proyecto_detalle.html', {'proyecto': proyecto, 'tareas': tareas})
    except ObjectDoesNotExist:
        crud_logger.error(f"Proyecto con id {id} no encontrado.")
        return render(request, 'tareas/error.html', {'message': 'Proyecto no encontrado'})
    except Exception as e:
        crud_logger.error(f"Error al cargar el proyecto: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al cargar el proyecto'})

def tarea_detalle(request, id):
    try:
        tarea = get_object_or_404(Tarea, id=id)
        crud_logger.debug(f"Tarea cargada: {tarea.nombre}")
        return render(request, 'tareas/tarea_detalle.html', {'tarea': tarea})
    except ObjectDoesNotExist:
        crud_logger.error(f"Tarea con id {id} no encontrada.")
        return render(request, 'tareas/error.html', {'message': 'Tarea no encontrada'})
    except Exception as e:
        crud_logger.error(f"Error al cargar la tarea: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al cargar la tarea'})

def proyecto_nuevo(request):
    try:
        if request.method == "POST":
            form = ProyectoForm(request.POST)
            if form.is_valid():
                proyecto = form.save()
                crud_logger.debug(f"Proyecto creado: {proyecto.nombre}")
                return redirect('proyecto_detalle', id=proyecto.id)
        else:
            form = ProyectoForm()
        return render(request, 'tareas/proyecto_nuevo.html', {'form': form})
    except ValidationError as e:
        crud_logger.error(f"Error de validación al crear el proyecto: {e}")
        return render(request, 'tareas/proyecto_nuevo.html', {'form': form, 'errors': e})
    except Exception as e:
        crud_logger.error(f"Error al crear el proyecto: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al crear el proyecto'})

def tarea_nueva(request, proyecto_id):
    try:
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
    except ObjectDoesNotExist:
        crud_logger.error(f"Proyecto con id {proyecto_id} no encontrado.")
        return render(request, 'tareas/error.html', {'message': 'Proyecto no encontrado'})
    except ValidationError as e:
        crud_logger.error(f"Error de validación al crear la tarea: {e}")
        return render(request, 'tareas/tarea_nueva.html', {'form': form, 'errors': e})
    except Exception as e:
        crud_logger.error(f"Error al crear la tarea: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al crear la tarea'})

def proyecto_editar(request, id):
    try:
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
    except ObjectDoesNotExist:
        crud_logger.error(f"Proyecto con id {id} no encontrado.")
        return render(request, 'tareas/error.html', {'message': 'Proyecto no encontrado'})
    except ValidationError as e:
        crud_logger.error(f"Error de validación al editar el proyecto: {e}")
        return render(request, 'tareas/proyecto_editar.html', {'form': form, 'errors': e})
    except Exception as e:
        crud_logger.error(f"Error al editar el proyecto: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al editar el proyecto'})

def tarea_editar(request, id):
    try:
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
    except ObjectDoesNotExist:
        crud_logger.error(f"Tarea con id {id} no encontrada.")
        return render(request, 'tareas/error.html', {'message': 'Tarea no encontrada'})
    except ValidationError as e:
        crud_logger.error(f"Error de validación al editar la tarea: {e}")
        return render(request, 'tareas/tarea_editar.html', {'form': form, 'errors': e})
    except Exception as e:
        crud_logger.error(f"Error al editar la tarea: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al editar la tarea'})

def proyecto_borrar(request, id):
    try:
        proyecto = get_object_or_404(Proyecto, id=id)
        proyecto.delete()
        crud_logger.debug(f"Proyecto borrado: {proyecto.nombre}")
        return redirect('index')
    except ObjectDoesNotExist:
        crud_logger.error(f"Proyecto con id {id} no encontrado.")
        return render(request, 'tareas/error.html', {'message': 'Proyecto no encontrado'})
    except Exception as e:
        crud_logger.error(f"Error al borrar el proyecto: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al borrar el proyecto'})

def tarea_borrar(request, id):
    try:
        tarea = get_object_or_404(Tarea, id=id)
        proyecto_id = tarea.proyecto.id
        tarea.delete()
        crud_logger.debug(f"Tarea borrada: {tarea.nombre}")
        return redirect('proyecto_detalle', id=proyecto_id)
    except ObjectDoesNotExist:
        crud_logger.error(f"Tarea con id {id} no encontrada.")
        return render(request, 'tareas/error.html', {'message': 'Tarea no encontrada'})
    except Exception as e:
        crud_logger.error(f"Error al borrar la tarea: {e}")
        return render(request, 'tareas/error.html', {'message': 'Error al borrar la tarea'})

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
