from django.urls import path
from apps.even import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
