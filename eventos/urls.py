from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventoList, name='lista_eventos'),
    path('crearE/', views.crear_evento, name='crear_evento'),
    path('organizadores/', views.organizadoresList.as_view(), name='organizadores'),
    path('organizadores/crearO', views.crear_organizador.as_view(), name='crear_organizador'),
]