from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import SponsorModel
from .forms import SponsorForm

from django.urls import reverse_lazy


class SponsorListView (ListView):
    model = SponsorModel
    context_object_name = 'sponsors'
    template_name = 'admin/sponsors/admin_sponsor_list.html'

class SponsorCreateView (CreateView):
    form_class = SponsorForm
    template_name = 'admin/sponsors/admin_sponsor_create.html'

    def form_valid (self, form):
        form.save()
        return super(SponsorCreateView, self).form_valid(form)

class SponsorDetailView (DetailView):
    model = SponsorModel
    context_object_name = 'sponsor'
    template_name = 'admin/sponsors/admin_sponsor_detail.html'

class SponsorUpdateView (UpdateView):
    model = SponsorModel
    fields = ('title', 'link', 'block', 'image')
    template_name = 'admin/sponsors/admin_sponsor_update.html'
    success_url = '/sponsor/list/'

class SponsorDeleteView (DeleteView):
    model = SponsorModel
    template_name = 'admin/sponsors/admin_sponsor_delete.html'
    success_url = reverse_lazy('sponsor_list')