from django.urls import path
from . import views
urlpatterns = [
    path('', views.EventosList.as_view(), name='lista_eventos'),
]