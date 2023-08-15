"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
    homeView,
    cartView,
    aboutView,
    contactView,
    productView,
    wishlistView,
    checkoutView,
    PageView,
    productDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', PageView.as_view(), name='admin_panel'),

    path('ad/', include('ad.urls')),
    path('faq/', include('faq.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('users.urls')),
    path('about/', include('about.urls')),
    path('brand/', include('brand.urls')),
    path('sponsor/', include('sponsor.urls')),
    path('category/', include('category.urls')),

    path('', homeView.as_view(), name='index'),
    path('cart/', cartView.as_view(), name='cart'),
    path('user/', include('django.contrib.auth.urls')),
    path('contact/', contactView.as_view(), name='contact'),
    path('product/', productView.as_view(), name='product'),
    path('wishlist/', wishlistView.as_view(), name='wishlist'),
    path('checkout/', checkoutView.as_view(), name='checkout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('product/detail/', productDetailView.as_view(), name='product_detail'),
] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
