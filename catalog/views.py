from django.views.generic import TemplateView, ListView, FormView
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404

from .models import Item, Category
from .forms import AddItemForm


class IndexView(TemplateView):
    template_name = 'catalog/base.html'


class CategoryItemsList(ListView):
    template_name = 'catalog/category_items.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Item.objects.filter(published=True, categories__slug__exact=slug)

    def get_context_data(self):
        context = super(CategoryItemsList, self).get_context_data()
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


class SearchView(ListView):
    template_name = 'catalog/search.html'
    paginate_by = 20

    def dispatch(self, request, **kwargs):
        term = self.request.GET.get('q')
        if not term:
            return redirect('index')
        self.term = term
        return super(SearchView, self).dispatch(request, **kwargs)

    def get_queryset(self, **kwargs):
        q = Q(title__icontains=self.term) | Q(description__icontains=self.term)
        items = Item.objects.filter(q)
        return items

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        context['term'] = self.request.GET.get('q')
        return context


class AddItemFormView(FormView):
    template_name = 'catalog/add_item_form.html'
    form_class = AddItemForm
