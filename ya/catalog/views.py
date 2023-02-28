from django.shortcuts import HttpResponse, render

from catalog.models import Item


def items_list(request):
    items = Item.objects.select_related('category')
    context = {'items': items}
    template = 'catalog/items_list.html'
    return render(request, template, context)


def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item': item}
    template = 'catalog/item_detail.html'
    return render(request, template, context)


def item_correct_url(request, pk):
    return HttpResponse(f'элемент {pk}')
