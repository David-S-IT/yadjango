from django.contrib import admin

from .models import Category, Item, Tag


@admin.register(Item)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'name',
        'is_published',
    )

    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    empty_value_display = '-пусто-'
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)


admin.site.register(Tag)
admin.site.register(Category)
