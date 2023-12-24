# PythonEmpleados
- este proyecto es para ingresar  Empleados con nuevas modificación para el registro 
- El proyecto se realizo netamente en PYTHON with DJANGO  


Ese es mi inicio en **PYTHYON** 

# Install

este proyecto  se necesita install '**_PYTHON_**'

## Comando para utilizar en "Django" se porne el comando 

- '_pip install django_'

## Para crear una "Proyecto" en PYTHON  
- Es con el comando "_django-admin startproject AppWebInicio_"

## Para crear una "Aplicación" en PYTHON  
- Es con el comanndo "_django-admin startapp app_"
  - Este comando se poner dentro de la carpeta "AppWebInicio"

## se a utilizado los comando de:
- primero se ejecuta este comando "py manage.py migrate" para tener la tabla creadas y después "py manage.py makemigrations "
## DATABASE:
- En este proyecto se utilizó MYSQL como base de datos y el nombre de la base de Datos "--unidb--"
  
## Para ejecutar este programa es con el
- comando "python manage.py runserver "

## rutas 
- path('', views.listarempleado, name='listarempleado'),
- path('insertar/', views.insertarempleado, name='insertarempleado'),
- path('editar/<int:id>', views.editarempleado, name='editarempleado'),
- path('modificar/<int:id>', views.modificarempleado, name='modificarempleado'),
- path('eliminar/<int:id>', views.eliminarempleado, name='eliminarempleado'),
