from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('Главная')
