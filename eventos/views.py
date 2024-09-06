from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm

def index(request):
    return render(request, 'index.html')
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

class organizadoresList(ListView):
    model = Organizador
    template_name = 'organizadores.html'
    context_object_name = 'organizadores'  # Nombre que se usará en el template para acceder a los organizadores

# Vista para crear un nuevo organizador
class crear_organizador(CreateView):
    model = Organizador
    form_class = OrganizadorForm  # Usamos el formulario OrganizadorForm
    template_name = 'organizadoresForm.html'
    success_url = reverse_lazy('organizadores')  # Redirige a la lista después de crear