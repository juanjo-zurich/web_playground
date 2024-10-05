from django.contrib.admin.views.decorators import staff_member_required

from django.utils.decorators import method_decorator

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    
    '''
    Este mixin require que el usuario sea miembro del staff
    '''
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)
    
    
# Create your views here.
class PagesListView(ListView):
    model = Page
    
    
class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page.html"
@method_decorator(staff_member_required, name='dispatch')    
class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages") # Redirecciona a la url

@method_decorator(staff_member_required, name='dispatch')  
class PageUpdate(StaffRequiredMixin, UpdateView):
     model = Page
     #fields = ["title", "content", 'order']
     form_class = PageForm
     template_name_suffix = "_update_form"
     
     
     def get_success_url(self) -> str:
         return reverse_lazy("pages:update", args = [ self.object.id]) + "?ok"

@method_decorator(staff_member_required, name='dispatch')  
class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")