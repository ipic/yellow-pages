from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile, Category, Item
from .forms import AdminAddItemForm


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
    list_display = ('title', 'description', 'slug')


def publish_item(modeladmin, request, queryset):
    for item in queryset:
        item.publish()
    messages.success(request, 'Itens publicados!')
publish_item.short_description = 'Publicar item'


class ItemAdmin(admin.ModelAdmin):
    model = Item
    form = AdminAddItemForm
    raw_id_fields = ('user', )
    list_display = ('title', 'address', 'website', 'published', )
    search_fields = ('title', 'categories__title', 'description', 'website')
    actions = [publish_item]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
