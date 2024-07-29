from django.contrib import admin

from .forms import MenuItemForm
from .models import Menu, MenuItem


class ItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fields = ['menu', 'title', 'parent', 'href', 'named_url']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    inlines = ItemInline,


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ('menu', 'title', 'parent', 'href', 'named_url')
    fields = ['menu', 'title', 'parent', 'href', 'named_url']
    inlines = ItemInline,
