from django.urls import path
from . import views
urlpatterns = [
    path('', views.eventoList, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
]