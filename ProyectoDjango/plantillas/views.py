from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm, ProductoForm, CustomUserCreationForm, ModificarProductoForm
from .models import Producto
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'plantillas/index.html', {'user':request.user})

def carro(request):
    productos = Producto.objects.all()
    return render(request, 'plantillas/carro.html', {'productos':productos})

def about(request):
    return render(request, 'plantillas/about.html')

def contact(request):
    data = {}
    if request.method=='POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"

    return render(request, 'plantillas/contact.html', data)

def services(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'plantillas/services.html', data)

def agregar_producto(request):
    data = {
        'form':ProductoForm()
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('administracion')
    return render(request,'plantillas/plan/agregar.html', data) 

def modificar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    data = {
        'form':ModificarProductoForm(instance=producto),
        'producto':producto
    }
    if request.method=='POST':
        formulario = ModificarProductoForm(instance=producto, data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('administracion')
        else:
            data['formulario']= formulario
            return render(request,'plantillas/plan/modificar.html', data) 
    return render(request,'plantillas/plan/modificar.html', data) 

def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect('index')

def login(request):
    if request.method=='POST':
        user=authenticate(request,username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'mensaje':'Credencial Invalida'})

        
    return render(request, 'registration/login.html')

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"]= formulario
    return render(request, 'registration/registro.html', data)

def es_superuser(user):
    return user.is_superuser

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def administracion(request):
    productos=Producto.objects.all()
    return render (request,'administracion.html', {'productos':productos})