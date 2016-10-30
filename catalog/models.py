from django.db import models
from django.contrib.auth.models import User


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
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Item(models.Model):
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição', blank=True)
    address = models.CharField('Endereço', max_length=255)
    phone = models.CharField('Telefone', max_length=20)
    website = models.URLField('Website', blank=True)
    email = models.URLField('Email', blank=True)
    published = models.BooleanField('Publicado', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
