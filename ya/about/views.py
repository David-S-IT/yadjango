from django.shortcuts import HttpResponse


def description(request):
    return HttpResponse('О проекте')
