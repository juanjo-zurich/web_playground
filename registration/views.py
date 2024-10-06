from django import forms
from .forms import UserCreationFormWhithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWhithEmail
    # success_url = reverse_lazy("login") # Normalmente es asi. pero como le queremos modificar el success_url sobreescribimos  def get_success_url(self)
    template_name = "registration/signup.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?register"
    
    def get_form(self, form_class=None):
        form  = super(SignUpView,self).get_form(form_class)
        # modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={"class":'form-control mb-2', 'placeholder':"Nombre de usuario"})
        form.fields['email'].widget = forms.EmailInput(attrs={"class":'form-control mb-2', 'placeholder':"Email"})
        form.fields['password1'].widget = forms.PasswordInput(attrs={"class":'form-control mb-2', 'placeholder':"Password"})
        form.fields['password2'].widget = forms.PasswordInput(attrs={"class":'form-control mb-2', 'placeholder':"Confirmar Password"})
        return form