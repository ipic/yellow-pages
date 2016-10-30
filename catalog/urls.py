from django.conf.urls import url

from .views import IndexView, CategoryItemsList, SearchView, AddItemFormView

urlpatterns = [
    url(r'^search/?$', SearchView.as_view(), name='search'),
    url(r'^adicionar/?$', AddItemFormView.as_view(), name='add-item'),
    url(r'^(?P<slug>[\w-]+)/?$', CategoryItemsList.as_view(), name='category-list'),
    url(r'^', IndexView.as_view(), name='index'),
]
