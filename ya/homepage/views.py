from django.db.models import Prefetch
from django.shortcuts import HttpResponse, render

from catalog.models import Item, Tag


def home(request):
    items = (
        Item.objects.select_related('category', 'main_image')
        .filter(
            is_published=True, is_on_main=True, category__is_published=True
        )
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
        .order_by('name')
    )
    context = {'items': items}
    template = 'homepage/index.html'
    return render(request, template, context)


def coffee(request):
    return HttpResponse('Я чайник', status=418)
