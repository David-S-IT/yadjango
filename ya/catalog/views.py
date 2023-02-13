from django.shortcuts import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, number):
    return HttpResponse('Подробно элемент')
