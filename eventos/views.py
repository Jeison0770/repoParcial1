from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento

class EventosList(ListView):
    model = Evento
    template_name = 'evento.html'
    context_object_name = 'eventos'