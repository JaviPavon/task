from django.shortcuts import render, redirect

from django.utils import timezone

from .models import Task

from .forms import TaskForm

def list_tasks(request):

    tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form=TaskForm()
    return render(request, 'task/list_tasks.html', {'tasks': tasks, 'form':form})