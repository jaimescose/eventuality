from django.urls import path
from even import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
