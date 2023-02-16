from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('Главная')


def coffee(request):
    return HttpResponse('Я чайник', status=418)
