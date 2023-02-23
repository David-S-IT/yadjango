from django.contrib import admin

from .models import Category, Item, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        Item.name.field.name,
        Item.is_published.field.name,
    )

    list_display_links = (Item.name.field.name,)
    empty_value_display = '-пусто-'
    list_editable = (Item.is_published.field.name,)
    filter_horizontal = (Item.tags.field.name,)


admin.site.register(Tag)
admin.site.register(Category)
