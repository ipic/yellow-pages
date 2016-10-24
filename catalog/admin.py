from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

from .models import Profile, Category, Item
from .widgets import GoogleMapsAddressWidget


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Informações adicionais'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_name', 'email', 'is_superuser')
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email')
        }),
    )
    inlines = (ProfileInline, )

    def get_name(self, obj):
        return obj.get_full_name()


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('title',), }


class ItemGMapForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'address': GoogleMapsAddressWidget,
        }


class ItemAdmin(admin.ModelAdmin):
    model = Item
    form = ItemGMapForm
    raw_id_fields = ('owner', )
    list_display = ('title', 'owner', 'published')
    search_fields = ('title', 'owner__first_name', 'owner__last_name',
                     'owner__email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
