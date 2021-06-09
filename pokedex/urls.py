from django.urls import path
from . import views
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PokedexListView.as_view(), name='pokemon-list'),
    path('pokemon-detail/<int:pk>', views.PokedexDetailView.as_view(), name='pokemon-detail'),
    path('pokemon-create/', views.PokedexCreateView.as_view(), name='pokemon-create'),
]
if settings:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)