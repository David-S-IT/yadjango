from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<body>Главная</body>')


def coffee(request):
    html_content = '<html><head><title>Coffee</title></head><body>'
    html_content += '<h1>Я чайник</h1>'
    html_content += '</body></html>'
    return HttpResponse(html_content, status=418)
