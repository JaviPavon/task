from django.shortcuts import render, redirect

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
        return render(request, self.nombre_template, {'tasks': self.actualizaTask(), 'form':form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            descripcion = form.cleaned_data['descripcion']
            fecha_creacion = form.cleaned_data['fecha_creacion']
            hecho = form.cleaned_data['hecho']
            Task.objects.create(
                title = title,
                descripcion = descripcion,
                fecha_creacion = fecha_creacion,
                hecho = hecho
            )
            # form.save()
            return redirect('list_tasks')
        return render(request, self.nombre_template, {'tasks': self.actualizaTask(), 'form':form})





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