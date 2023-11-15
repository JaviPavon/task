from django.urls import path

from .views import ListClass, TaskDetalles, CreacionTask, EditarTask, EliminarTask

urlpatterns = [

path('', ListClass.as_view(), name='list_tasks'),
path('task/<int:pk>/', TaskDetalles.as_view(), name='task_details'),
path('task/Creacion/', CreacionTask.as_view(), name='task_creation'),
path('task/Editar/<int:pk>', EditarTask.as_view(), name='task_edition'),
path('delete/<int:pk>/',EliminarTask.as_view(),name='delete'),
]