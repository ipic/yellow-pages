from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (IndexView, CategoryItemsList, SearchView, AddItemFormView,
                    ContactFormView, ItemView)

urlpatterns = [
    url(r'^search/?$', SearchView.as_view(), name='search'),
    url(r'^adicionar/sucesso$',
        TemplateView.as_view(template_name='catalog/add_item_success.html'),
        name='add-success'),
    url(r'^adicionar/?$', AddItemFormView.as_view(), name='add-item'),
    url(r'^contato/?$', ContactFormView.as_view(), name='contact'),
    url(r'^ver/(?P<slug>[\w-]+)/?$', ItemView.as_view(), name='item-detail'),
    url(r'^(?P<slug>[\w-]+)/?$', CategoryItemsList.as_view(),
        name='category-list'),
    url(r'^', IndexView.as_view(), name='index'),
]
