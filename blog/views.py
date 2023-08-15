from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BlogModel, BlogImageModel, BlogCommentModel
from .forms import BlogForm, BlogImageForm, BlogCommentForm, BlogCommentUpdateForm

class UserBlogList (ListView):
    model = BlogModel
    context_object_name = 'blogs'
    template_name = 'user/blog.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        blogs = BlogModel.objects.filter(block=False).order_by('-created_at')
        blog_images = BlogImageModel.objects.filter(block=False).order_by('sequence_number')

        return render(request, self.template_name, {'blogs': blogs, 'blog_images': blog_images})
        
class UserBlogDetail (FormView):
    model = BlogModel
    form_class = BlogCommentForm
    context_object_name = 'blog'
    queryset = BlogModel.objects.all()
    template_name = 'user/blog_detail.html'

    def get (self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        blog = BlogModel.objects.filter(pk=pk, block=False).first()
        blog_images = BlogImageModel.objects.filter(blog=pk, block=False).order_by('sequence_number')
        blog_comments = BlogCommentModel.objects.filter(blog=pk, block=False).order_by('-created_at')

        # l = BlogModel.objects.filter(block=False)
        # k = BlogCommentModel.objects.filter(blog=i.pk for i in l)
        # print(k)
        # blogs = BlogCommentModel.objects.all()
        # blogss = BlogModel.objects.all()
        # j = 0
        # count = 0
        # for i in range(0, len(blogs)):

        #     if blogs[i].blog.pk == blogss[j].pk:
        #         count += 1
            
        # print(count, len(blogs))
        return render(request, self.template_name, {'blog': blog, 'blog_images': blog_images, 'blog_comments': blog_comments, 'form': self.form_class})


class BlogListView (ListView):
    model = BlogModel
    context_object_name = 'blogs'
    template_name = 'admin/blogs/admin_blog_list.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        blogs = BlogModel.objects.all()
        blog_images = BlogImageModel.objects.all()

        return render(request, self.template_name, {'blogs': blogs, 'blog_images': blog_images})

class BlogCreateView (CreateView):
    form_class = BlogForm
    template_name = 'admin/blogs/admin_blog_create.html'

    def form_valid (self, form):
        form.instance.author = self.request.user
        form.save()
        return super(BlogCreateView, self).form_valid(form)

class BlogDetailView (DetailView):
    model = BlogModel
    form_class = BlogCommentForm
    context_object_name = 'blog'
    queryset = BlogModel.objects.all()
    template_name = 'admin/blogs/admin_blog_detail.html'

    def get (self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        blogs = BlogModel.objects.filter(pk=pk).first()
        blog_images = BlogImageModel.objects.filter(blog=pk).order_by('sequence_number')
        blog_comments = BlogCommentModel.objects.filter(blog=pk).order_by('-created_at')

        return render(request, self.template_name, {'blog': blogs, 'blog_images': blog_images, 'blog_comments': blog_comments, 'form': self.form_class})

class BlogUpdateView (UpdateView):
    model = BlogModel
    fields = ('title', 'description', 'block')
    template_name = 'admin/blogs/admin_blog_update.html'
    success_url = '/blog/list/'

class BlogDeleteView (DeleteView):
    model = BlogModel
    template_name = 'admin/blogs/admin_blog_delete.html'
    success_url = reverse_lazy('blog_list')


class BlogImageCreateView (FormView):
    model = BlogImageModel
    form_class = BlogImageForm
    queryset = BlogImageModel.objects.all()

    template_name = 'admin/blogs/admin_blog_image_create.html'
    success_url = '/blog/list/'

    def form_valid(self, form: Any) -> HttpResponse:
        blog = BlogModel.objects.get(pk=self.kwargs.get('pk'))
        BlogImageModel.objects.create(
            image = form.cleaned_data['image'],
            sequence_number = form.cleaned_data['sequence_number'],
            blog = blog  
        )

        return super(BlogImageCreateView, self).form_valid(form)

class BlogImageDetailView (DetailView):
    model = BlogImageModel
    template_name = 'admin/blogs/admin_blog_image_detail.html'
    success_url = '/blog/list/'

class BlogImageUpdateView (UpdateView):
    model = BlogImageModel
    template_name = 'admin/blogs/admin_blog_image_update.html'
    fields = ('sequence_number', 'block', 'image')
    success_url = '/blog/list/'

class BlogImageDeleteView (DeleteView):
    model = BlogImageModel
    template_name = 'admin/blogs/admin_blog_delete.html'
    success_url = reverse_lazy('blog_list')


class BlogCommentCreateView (FormView):
    model = BlogCommentModel
    form_class = BlogCommentForm
    template_name = 'admin/blogs/admin_blog_detail.html'

    def form_valid(self, form: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            blog = BlogModel.objects.filter(pk=self.kwargs.get('pk')).first()
            BlogCommentModel.objects.create(
            blog = blog,
            user = self.request.user,
            message = form.cleaned_data['message']
            )

            if self.request.user.is_superuser:
                return redirect('/blog/detail/'+ str(self.kwargs.get('pk')))
            else:  
                return redirect('/blog/user/detail/'+ str(self.kwargs.get('pk')))
        return redirect('/user/login/')

class BlogCommentUpdateView (UpdateView):
    model = BlogCommentModel
    form_class = BlogCommentUpdateForm
    template_name = 'admin/blogs/admin_blog_comment_update.html'

class BlogCommentDeleteView (DeleteView):
    model = BlogCommentModel
    template_name = 'admin/blogs/admin_blog_delete.html'
    success_url = reverse_lazy('blog_list')
