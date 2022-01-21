from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Shopvisor-Explore'),
    path('about/', views.about, name='Shopvisor-About'),
    path('shop/', views.shop, name='Shopvisor-Shop'),

]