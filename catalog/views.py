from django.views.generic import TemplateView, ListView

from .models import Item


class IndexView(TemplateView):
    template_name = 'catalog/base.html'


class CategoryItemsList(ListView):
    template_name = 'catalog/category_items.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Item.objects.filter(published=True, categories__slug__exact=slug)
