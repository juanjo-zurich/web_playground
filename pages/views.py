from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page
    
    
class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page.html"
    
class PageCreate(CreateView):
    model = Page
    fields = ["title", "content", 'order']

