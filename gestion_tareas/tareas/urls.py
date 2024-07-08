# tareas/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'proyectos', views.ProyectoViewSet)
router.register(r'tareas', views.TareaViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.index, name='index'),
    path('proyecto/<int:id>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('tarea/<int:id>/', views.tarea_detalle, name='tarea_detalle'),
    path('proyecto/nuevo/', views.proyecto_nuevo, name='proyecto_nuevo'),
    path('tarea/nueva/<int:proyecto_id>/', views.tarea_nueva, name='tarea_nueva'),
    path('proyecto/<int:id>/editar/', views.proyecto_editar, name='proyecto_editar'),
    path('tarea/<int:id>/editar/', views.tarea_editar, name='tarea_editar'),
    path('proyecto/<int:id>/borrar/', views.proyecto_borrar, name='proyecto_borrar'),
    path('tarea/<int:id>/borrar/', views.tarea_borrar, name='tarea_borrar'),
    path('API/', include(router.urls)),
]
