from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'organizador']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if 'Cancelado' in nombre:
            raise forms.ValidationError('El nombre no puede ser "Cancelado".')
        return nombre
