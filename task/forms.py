from django import forms
from .models import Task
from django.utils import timezone


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = {'title','descripcion'}


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha_creacion = forms.DateTimeField(initial=timezone.now)
    hecho = forms.BooleanField(required=False)
