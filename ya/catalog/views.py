from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def items_list(request):
    items = Item.objects.items_queryset().order_by(Item.category.field.name)
    context = {'items': items}
    template = 'catalog/items_list.html'
    return render(request, template, context)


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.items_queryset(), id=pk)
    context = {'item': item}
    template = 'catalog/item_detail.html'
    return render(request, template, context)
