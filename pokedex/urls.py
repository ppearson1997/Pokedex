from django.urls import path
from . import views

urlpatterns = [
    path('', views.PokedexListView.as_view(), name='pokemon-list'),
    path('pokemon-detail/<int:pk>', views.PokedexDetailView.as_view(), name='pokemon-detail'),
    path('pokemon-create/', views.PokedexCreateView.as_view(), name='pokemon-create'),
]