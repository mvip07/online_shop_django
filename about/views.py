from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from .forms import CompanyFileForm, CompanyMemberForm
from .models import CompanyFileModel, CompanyMemberModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView, FormView, DetailView

# Create your views here.
class AdminAboutView (ListView):
    model = CompanyFileModel
    template_name = 'admin/abouts/admin_about_list.html'

    def get (self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        companyFiles = CompanyFileModel.objects.all()
        companyMembers = CompanyMemberModel.objects.all()

        CFL = []
        CML = []

        for i in companyFiles:
            CFL.append(CompanyFileModel.get_req(i))

        for i in companyMembers:
            CML.append(CompanyMemberModel.get_req(i))
        
        return render(request, self.template_name, {'files': CFL, 'members': CML})

class UserAboutView (ListView):
    model = CompanyFileModel
    template_name = 'user/about.html'

    def get (self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        companyFiles = CompanyFileModel.objects.all()
        companyMembers = CompanyMemberModel.objects.all()

        CFL = []
        CML = []

        for i in companyFiles:
            CFL.append(CompanyFileModel.get_req(i))

        for i in companyMembers:
            CML.append(CompanyMemberModel.get_req(i))
        
        return render(request, self.template_name, {'files': CFL, 'members': CML})

class CompanyFileCreateView (CreateView):
    form_class = CompanyFileForm
    template_name = 'admin/abouts/admin_about_create.html'
    success_url = '/about/list/'

    def form_valid(self, form):
        form.save()
        return super(CompanyFileCreateView, self).form_valid(form)

class CompanyFileUpdateView (UpdateView):
    model = CompanyFileModel
    template_name = 'admin/abouts/admin_about_update.html'
    fields = ('title', 'image', 'block')
    success_url = '/about/list'

class CompanyFileDetailView (DetailView):
    model = CompanyFileModel
    context_object_name = 'file'
    template_name = 'admin/abouts/admin_about_file_detail.html'

class CompanyFileDeleteView (DeleteView):
    model = CompanyFileModel
    template_name = 'admin/abouts/admin_about_delete.html'
    success_url = reverse_lazy('about_list')

class CompanyMemberCreateView (CreateView):
    form_class = CompanyMemberForm
    template_name = 'admin/abouts/admin_about_create.html'
    success_url = '/about/list/'

    def form_valid(self, form):
        form.save()
        return super(CompanyMemberCreateView, self).form_valid(form)

class CompanyMemberUpdateView (UpdateView):
    model = CompanyMemberModel
    template_name = 'admin/abouts/admin_about_update.html'
    fields = ('first_name', 'last_name', 'email', 'phone', 'job', 'block', 'image')
    success_url = '/about/list'

class CompanyMemberDetailView (DetailView):
    model = CompanyMemberModel
    context_object_name = 'member'
    template_name = 'admin/abouts/admin_about_member_detail.html'

class CompanyMemberDeleteView (DeleteView):
    model = CompanyMemberModel
    template_name = 'admin/abouts/admin_about_delete.html'
    success_url = reverse_lazy('about_list')