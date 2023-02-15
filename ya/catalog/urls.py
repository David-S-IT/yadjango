from django.urls import path, re_path, register_converter

from . import converter, views

register_converter(converter.PositiveIntegerConverter, 'PosIntConv')

app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('converter/<PosIntConv:pk>/', views.item_detail, name='item_detail'),
    re_path(r'^re/(?P<pk>[1-9]\d*)/$', views.item_detail, name='item_detail'),
]
