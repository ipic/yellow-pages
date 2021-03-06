from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import Item, Category
from .forms import AddItemForm, ContactForm


class IndexView(TemplateView):
    template_name = 'catalog/base.html'

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class CategoryItemsList(ListView):
    template_name = 'catalog/category_items.html'
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Item.objects.filter(published=True, categories__slug__exact=slug)

    def get_context_data(self):
        context = super(CategoryItemsList, self).get_context_data()
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


class ItemView(DetailView):
    model = Item
    template_name = 'catalog/item.html'
    context_object_name = 'item'


class SearchView(ListView):
    template_name = 'catalog/search.html'
    paginate_by = 20
    context_object_name = 'items'

    def dispatch(self, request, **kwargs):
        term = self.request.GET.get('q')
        if not term:
            return redirect('index')
        self.term = term
        return super(SearchView, self).dispatch(request, **kwargs)

    def get_queryset(self, **kwargs):
        q = Q(title__icontains=self.term)
        q |= Q(description__icontains=self.term)
        q |= Q(address__icontains=self.term)
        q &= Q(published=True)
        items = Item.objects.filter(q)
        return items

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        context['term'] = self.request.GET.get('q')
        return context


class AddItemFormView(FormView):
    template_name = 'catalog/add_item_form.html'
    form_class = AddItemForm

    def form_valid(self, form):
        form.save()
        return redirect('add-success')


class ContactFormView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Sua mensagem foi enviada! '
                         'Obrigado pelo contato. Iremos responder o mais '
                         'rápido possível')
        return redirect('contact')
