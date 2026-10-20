from django.urls import path

from . import views

app_name = 'cartaspokemon'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('raridade/<int:raridade_id>/', views.cartas_por_raridade, name='cartas_por_raridade'),
]
