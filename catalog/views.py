from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'catalog/base.html'
