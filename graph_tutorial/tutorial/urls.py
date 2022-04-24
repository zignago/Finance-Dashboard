from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('search', views.graph, name='home2'),
]
