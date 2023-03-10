from django.db import models


class ItemManager(models.Manager):
    def items_queryset(self):
        from .models import Item, Tag

        return (
            self.get_queryset()
            .select_related(
                Item.category.field.name, Item.main_image.related.name
            )
            .filter(is_published=True, category__is_published=True)
            .prefetch_related(
                models.Prefetch(
                    Item.tags.field.name,
                    queryset=Tag.objects.filter(is_published=True).only(
                        Tag.name.field.name
                    ),
                )
            )
            .only(
                Item.name.field.name,
                Item.text.field.name,
                Item.category.field.name + '__name',
            )
        )
