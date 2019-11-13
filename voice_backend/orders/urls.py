from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transfer/', views.audio_transfer),
    path('flow/', views.flow_order)
]