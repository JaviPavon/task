from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

from django.views import View

from .models import Task

from .forms import TaskForm


class ListClass(View):
    
    nombre_template = 'task/list_tasks.html'
    tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')

    def actualizaTask(self):
        self.task = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
        return self.task
        
    def get(self, request):
        form = TaskForm()
        return render(request, self.nombre_template, {'tasks': self.actualizaTask()})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # descripcion = form.cleaned_data['descripcion']
            # fecha_creacion = form.cleaned_data['fecha_creacion']
            # hecho = form.cleaned_data['hecho']
            # Task.objects.create(
            #     title = title,
            #     descripcion = descripcion,
            #     fecha_creacion = fecha_creacion,
            #     hecho = hecho
            # )
            form.save()
            return redirect('list_tasks')
        return render(request, self.nombre_template, {'tasks': self.actualizaTask()})
    


class TaskDetalles(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return render(request, 'task/task_details.html', {'task': task})

    
class CreacionTask(View):
    
    nombre_template = 'task/task_creation.html'
    tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')

        
    def get(self, request):
        form = TaskForm()
        return render(request, self.nombre_template, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # descripcion = form.cleaned_data['descripcion']
            # fecha_creacion = form.cleaned_data['fecha_creacion']
            # hecho = form.cleaned_data['hecho']
            # Task.objects.create(
            #     title = title,
            #     descripcion = descripcion,
            #     fecha_creacion = fecha_creacion,
            #     hecho = hecho
            # )
            form.save()
            return redirect('list_tasks')
        return render(request, self.nombre_template, {'form':form})

class EditarTask(View):
    http_method_names = ['get', 'post', 'delete']
    nombre_template = 'task/task_edit.html'
    
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        return render(request, self.nombre_template, {'form': form, 'task': task})

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # descripcion = form.cleaned_data['descripcion']
            # fecha_creacion = form.cleaned_data['fecha_creacion']
            # hecho = form.cleaned_data['hecho']
            # Task.objects.create(
            #     title = title,
            #     descripcion = descripcion,
            #     fecha_creacion = fecha_creacion,
            #     hecho = hecho
            # )
            form.save()
            return redirect('list_tasks')
        return render(request, self.nombre_template, {'form':form, 'task': task})

class EliminarTask(View):
    nombre_template = 'task/task_delete.html'
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return render(request, self.nombre_template, {'task': task})
    def post(self,  request,pk):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect('list_tasks')
    
# def list_tasks(request):

#     tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
#     if request.method == 'POST':
#         form=TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_tasks')
#     else:
#         form=TaskForm()
#     return render(request, 'task/list_tasks.html', {'tasks': tasks, 'form':form})