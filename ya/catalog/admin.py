from django.contrib import admin

from .models import Category, GalleryImage, Item, MainImage, Tag


class MainImageInline(admin.TabularInline):
    model = MainImage
    readonly_fields = ('image_tmb',)
    fields = ('image', 'image_tmb')


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    readonly_fields = ('image_tmb',)
    fields = ('image', 'image_tmb')
    extra = 3


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        Item.name.field.name,
        Item.is_published.field.name,
        Item.main_image_tmb,
        Item.is_on_main.field.name,
    )
    empty_value_display = '-пусто-'
    inlines = (MainImageInline, GalleryImageInline)
    list_display_links = (Item.name.field.name,)
    list_editable = (Item.is_published.field.name, Item.is_on_main.field.name)
    filter_horizontal = (Item.tags.field.name,)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')


@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')


admin.site.register(Tag)
admin.site.register(Category)
