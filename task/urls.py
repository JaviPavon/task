from django.urls import path

from .views import ListClass

urlpatterns = [

path('', ListClass.as_view(), name='list_tasks'),

]