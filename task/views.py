from django.shortcuts import render

from django.utils import timezone

from .models import Task

def list_tasks(request):

    tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'task/list_tasks.html', {'tasks': tasks})