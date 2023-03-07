from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag


def items_list(request):
    items = (
        Item.objects.select_related('category', 'main_image')
        .filter(is_published=True, category__is_published=True)
        .prefetch_related(
            Prefetch(
                'tags', queryset=Tag.objects.all().filter(is_published=True)
            )
        )
        .only(
            'name',
            'text',
            'category__name',
        )
        .order_by('category')
    )
    context = {'items': items}
    template = 'catalog/items_list.html'
    return render(request, template, context)


def item_detail(request, pk):
    item = get_object_or_404(
        Item.objects.select_related('category', 'main_image'), id=pk
    )
    context = {'item': item}
    template = 'catalog/item_detail.html'
    return render(request, template, context)
