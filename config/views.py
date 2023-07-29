from django.views.generic import TemplateView

class homeView (TemplateView):
    template_name = 'user/index.html'

class aboutView (TemplateView):
    template_name = 'user/about.html'

class blogView (TemplateView):
    template_name = 'user/blog.html'

class blogDetailView (TemplateView):
    template_name = 'user/blog_detail.html'

class cartView (TemplateView):
    template_name = 'user/cart.html'

class contactView (TemplateView):
    template_name = 'user/contact.html'

class faqView (TemplateView):
    template_name = 'user/faq.html'

class checkoutView (TemplateView):
    template_name = 'user/checkout.html'

class productView (TemplateView):
    template_name = 'user/product.html'

class productDetailView (TemplateView):
    template_name = 'user/product_detail.html'

class wishlistView (TemplateView):
    template_name = 'user/wishlist.html'

class adminPageView (TemplateView):
    template_name = 'admin/index.html'


