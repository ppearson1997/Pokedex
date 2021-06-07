from django.urls import path
from . import views

urlpatterns = [
    path('', views.PokedexListView.as_view(), name='pokemon-list'),
]