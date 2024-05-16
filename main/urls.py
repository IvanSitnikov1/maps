from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.one, name='1'),
    path('2/', views.two, name='2'),
    path('3/', views.three, name='3'),
]
