from django.shortcuts import HttpResponse


def item_list(request):
    return HttpResponse('<body>Список элементов</body>')


def item_detail(request, pk):
    return HttpResponse(f'<body>Подробно элемент: {pk}</body>')


def re_digit(request, pk):
    return HttpResponse(f'Номер {pk}')
