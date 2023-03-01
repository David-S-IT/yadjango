from django.urls import path, re_path, register_converter

from . import converter, views

register_converter(converter.PositiveIntegerConverter, 'PosIntConv')

app_name = 'catalog'

urlpatterns = [
    path('', views.items_list, name='items_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path(
        'converter/<PosIntConv:pk>/',
        views.item_detail,
        name='converter_item_detail',
    ),
    re_path(
        r'^re/(?P<pk>[1-9]\d*)/$',
        views.item_detail,
        name='regex_item_detail',
    ),
]
