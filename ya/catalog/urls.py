from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_list),
    path('<int:number>', views.item_detail),
]
