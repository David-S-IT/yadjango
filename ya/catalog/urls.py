from django.urls import path, re_path, register_converter

from . import converter, views

register_converter(converter.PositiveIntegerConverter, 'PosIntConv')

app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='catalog'),
    path('<int:pk>/', views.item_detail, name='catalog_pk'),
    path('converter/<PosIntConv:pk>/', views.item_detail, name='converter_pk'),
    re_path(r'^re/(?P<pk>[1-9]\d*)/$', views.item_detail, name='re_pk'),
]
