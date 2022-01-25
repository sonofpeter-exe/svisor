from django.urls import path
from . import views

urlpatterns = [
    path('sort/', views.sort, name='sort-data'),
]
