from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Prueba de diccionario de contexto'
        return context'''
    
    def get(self, request, *args, **kwargs): # Reescribimos la respuesta y le mandamos el contexto(datos)
        return render(request, self.template_name, {'title': "Prueba de diccionario de contexto2"})

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'