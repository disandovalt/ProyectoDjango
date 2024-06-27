from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', "first_name", "last_name", "email", "password1", "password2"]

class ModificarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    def init(self, args, **kwargs):
        super(ModificarProductoForm, self).init(args, **kwargs)
        self.fields['imagen'].required = False

