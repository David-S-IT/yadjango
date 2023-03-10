from django.shortcuts import HttpResponse, render

from catalog.models import Item


def home(request):
    items = (
        Item.objects.items_queryset()
        .filter(
            is_on_main=True,
        )
        .order_by(Item.name.field.name)
    )
    context = {'items': items}
    template = 'homepage/index.html'
    return render(request, template, context)


def coffee(request):
    return HttpResponse('Я чайник', status=418)
