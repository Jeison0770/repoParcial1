from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Evento
from .forms import EventoForm

def eventoList(request):
    eventos = Evento.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventoForm.html', {'form': form})

