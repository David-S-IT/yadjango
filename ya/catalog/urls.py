from django.urls import path, re_path, register_converter

from . import converter, views

register_converter(converter.PositiveIntegerConverter, 'PosIntConv')

urlpatterns = [
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
    re_path(r'^re/(?P<pk>[1-9]\d*)/$', views.re_digit),
    path('converter/<PosIntConv:pk>/', views.converter_re_digit),
]
