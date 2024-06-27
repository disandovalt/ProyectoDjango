from django.urls import path
from . import views
from .views import index, about,  carro, contact, services, agregar_producto, modificar_producto, eliminar_producto, registro, login, cerrar_sesion, administracion
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('carro/', carro, name='carro'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('agregar_producto/',agregar_producto, name="agregar_producto"),
    path('modificar_producto/<int:id_producto>',modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<int:id_producto>',eliminar_producto, name="eliminar_producto"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('administracion', administracion, name="administracion")
]