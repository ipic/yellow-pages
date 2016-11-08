from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # profiles
    facebook_url = models.URLField('Facebok:', blank=True)
    twitter_url = models.URLField('Twitter:', blank=True)
    website_url = models.URLField('Página Pessoal:', blank=True)

    def __str__(self):
        return '{} {} <{}>'.format(self.user.get_full_name(), self.user.email)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-list', args=[self.slug])

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Item(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', null=True,
                             blank=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    title = models.CharField('Título', max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField('Descrição', blank=True)
    address = models.CharField('Endereço', max_length=255)
    location = geo_models.PointField('Localização')
    phone = models.CharField('Telefone', max_length=20)
    website = models.URLField('Website', blank=True)
    email = models.EmailField('Email')
    published = models.BooleanField('Publicado', default=False)

    objects = geo_models.GeoManager()

    def __str__(self):
        return self.title

    def publish(self):
        if self.published:
            return

        self.published = True
        self.save(update_fields=['published'])
        message = """
Olá!

Acabamos de publicar seu item no nosso sistema.

Nome: {}
Endereço: {}
Telefone: {}
Site: {}

""".format(self.title, self.address, self.phone, self.website)
        send_mail('[BUSQIPIC] Seu serviço foi publicado', message,
                  settings.DEFAULT_FROM_EMAIL, [self.email])

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
