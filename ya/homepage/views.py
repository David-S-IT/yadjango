from django.shortcuts import HttpResponse, render


def home(request):
    template = 'homepage/index.html'
    return render(request, template)


def coffee(request):
    return HttpResponse('Я чайник', status=418)
