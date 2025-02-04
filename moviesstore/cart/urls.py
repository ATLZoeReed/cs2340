from django.urls import path

from accounts.urls import urlpatterns
from . imports views

urlpatterns = [
    path('<int:id>/add/', views.add, name = 'cart.add'),
    path('', views.index, name='cart.index'),
    path('clear/', views.clear, name='cart.clear'),
]