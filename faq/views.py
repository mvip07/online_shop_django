from django.shortcuts import render


from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView

from .forms import FaqForm
from .models import FaqModel

from django.urls import reverse_lazy

# Create your views here.

class UserFaqListView (ListView):
    model = FaqModel
    context_object_name = 'faqs'
    template_name = 'user/faq.html'

class FaqListView (ListView):
    model = FaqModel
    context_object_name = 'faqs'
    template_name = 'admin/faqs/admin_faq_list.html'

class FaqCreateView (CreateView):
    form_class = FaqForm
    template_name = 'admin/faqs/admin_faq_create.html'

    def form_valid (self, form):
        form.save()
        return super (FaqCreateView, self).form_valid(form)

class FaqUpdateView (UpdateView):
    model = FaqModel
    template_name = 'admin/faqs/admin_faq_update.html'
    fields = ('question', 'answer', 'block')
    success_url = '/faq/list/'

class FaqDetailView (DetailView):
    model = FaqModel
    context_object_name = 'faq'
    template_name = 'admin/faqs/admin_faq_detail.html'

class FaqDeleteView (DeleteView):
    model = FaqModel
    template_name = 'admin/faqs/admin_faq_delete.html'
    success_url = reverse_lazy('faq_list')

