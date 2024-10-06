from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWhithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obligatorio, 254 caracteres como maxiom y debe ser válido.")

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")
    
    # Añadimos comprobacion a email    
    def clean_email(self):
        email = self.cleaned_data.get("email") # Recuperamos el email del formulario
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro.")
        return email