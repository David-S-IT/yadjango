from django.db import models
from django.db.models import Prefetch


class ItemManager(models.Manager):
    def items_queryset(self):
        from .models import Tag

        return (
            self.get_queryset()
            .select_related('category', 'main_image')
            .filter(is_published=True, category__is_published=True)
            .prefetch_related(
                Prefetch(
                    'tags',
                    queryset=Tag.objects.all().filter(is_published=True),
                )
            )
            .only(
                'name',
                'text',
                'category__name',
            )
        )
