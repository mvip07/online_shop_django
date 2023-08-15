from django.shortcuts import render


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy

from .forms import AdForm
from .models import AdModel

# Create your views here.

class AdListView (ListView):
    model = AdModel
    context_object_name = 'ads'
    template_name = 'admin/ads/admin_ad_list.html'

class AdCreateView (CreateView):
    form_class = AdForm
    template_name = 'admin/ads/admin_ad_create.html'

    def form_valid (self, form):
        form.save()
        return super(AdCreateView, self).form_valid(form)

class AdDetailView (DetailView):
    model = AdModel
    context_object_name = 'ad'
    template_name = 'admin/ads/admin_ad_detail.html'

class AdUpdateView (UpdateView):
    model = AdModel
    fields = ('link', 'block', 'image')
    template_name = 'admin/ads/admin_ad_update.html'
    success_url = '/ad/list/'

class AdDeleteView (DeleteView):
    model = AdModel
    template_name = 'admin/ads/admin_ad_delete.html'
    success_url = reverse_lazy('ad_list')

