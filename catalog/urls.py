from django.conf.urls import url

from .views import IndexView, CategoryItemsList

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/?$', CategoryItemsList.as_view(), name='category-list'),
    url(r'^', IndexView.as_view(), name='index'),
]
