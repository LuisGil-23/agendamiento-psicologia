from django import forms
from .models import Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['tipo','modalidad','fecha_hora','duracion_minutos','motivo']
        widgets = {'fecha_hora': forms.DateTimeInput(attrs={'type':'datetime-local'})}
