from django.views.generic import TemplateView


class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = 'index.html'


class ContactView(TemplateView):
    http_method_names = ['get']
    template_name = 'contact.html'


class PostView(TemplateView):
    http_method_names = ['get']
    template_name = 'post.html'
