from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('?12Список.элементов раз,два:три!(четыре)')


def coffee(request):
    return HttpResponse('Я чайник', status=418)
