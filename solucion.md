Crear un entorno virtual llamado task

```bash
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv task
```
Activo el entorno virtual en la terminal de Visual para trabajar en ella

```bash
source /home/alumnado/.virtualenvs/task/bin/activate
```

Actualizo Pip

```bash
python -m pip install --upgrade pip
```

Creo un requirements.txt en el directorio en el que estamos trabajando con lo que queramos instalar, en este caso: Django~=3.2.10
Y ejecutamos

```bash
pip install -r requirements.txt
```

Para empezar el proyecto ejecutaremos lo siguiente

```bash
django-admin startproject proyecto .
```

Cambiamos la Zona horaria y el idioma

```python
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Berlin'
```

Añadimos una ruta para archivos estáticos

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```

Introducimos el ip al que queremos relacionar nuestra aplicación

```python
ALLOWED_HOSTS = ['127.0.0.1']
```

Creamos la Base de datos

```bash
python manage.py migrate
```

Iniciamos el servidor Web

```bash
python manage.py runserver
```

Creamos la aplicación

```bash
python manage.py startapp task
```
Modificamos el settings.py y le introducimos nuestro task

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```

Modificamos el models.py

```python
from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):

    title = models.CharField(max_length=200)

    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return self.title
```

Aplicamos los cambios del modelo en la Base de Datos

```bash
python manage.py makemigrations task
#Prepara un fichero de migración
python manage.py migrate task
#Aplica un fichero de migración
```

Modificamos admin.py

```python
from django.contrib import admin

from .models import Task

admin.site.register(Task)
```

Creamos el SuperUsuario

```bash
python manage.py createsuperuser
```

Modificamos el views.py

```python
from django.shortcuts import render

from django.utils import timezone

from .models import Task

def post_list(request):

    tasks = Task.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'task/list_tasks.html', {'tasks': tasks})
```

Creamos un html en task/templates/task/list_task.html

```html
{% extends 'task/base.html' %}

<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>
{% block content %}
    {% for task in tasks %}

        <div>
            <p> publicado: {{ task.fecha_creacion }}</p>
            <h2><a href="">{{ task.title }}</a></h2>
            <p>{{ task.descripcion|linebreaksbr }}</p>
        </div>

    {% endfor %}
{% endblock %}
```

Creamos un html en task/templates/task/base.html

```html
<body>
    <div class="page-header">
        <h1><a href="/">Tareas Pavón</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
                {% block content %}
                
                {% endblock %}
            </div>

        </div>
    </div>
</body>
```

Modificamos urls.py de proyecto

```python
from django.contrib import admin

from django.urls import path, include

urlpatterns = [

path('admin/', admin.site.urls),

path('', include('task.urls')),

]
```

Modificamos urls.py de task

```python
from django.urls import path

from . import views

urlpatterns = [

path('', views.list_tasks, name='list_tasks'),

]
```
