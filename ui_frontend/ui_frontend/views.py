from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Try to import existing models; if not found, use sample data for the templates to render.
try:
    from psicologas.models import Psicologa
except Exception:
    Psicologa = None
try:
    from citas.models import Cita
except Exception:
    Cita = None

def login_view(request):
    # This view renders a modern login form that can authenticate via existing backend.
    # It expects the project to handle authentication (e.g., using Django auth).
    return render(request, 'ui_frontend/login.html', {})

def home_view(request):
    # Simple dashboard
    return render(request, 'ui_frontend/home.html', {})

def psicologas_list_view(request):
    # Attempt to fetch from model, otherwise show placeholder data.
    psicologas = []
    if Psicologa is not None:
        try:
            psicologas = list(Psicologa.objects.all()[:50])
        except Exception:
            psicologas = []
    if not psicologas:
        psicologas = [
            {'nombre': 'Dra. Ana Pérez', 'especialidad': 'Terapia Cognitivo-Conductual', 'foto_url': None, 'descripcion': 'Especialista en ansiedad y depresión.'},
            {'nombre': 'Dra. Laura Gómez', 'especialidad': 'Psicoterapia Infantil', 'foto_url': None, 'descripcion': 'Atención a niños y adolescentes.'},
        ]
    return render(request, 'ui_frontend/psicologas_list.html', {'psicologas': psicologas})

def citas_list_view(request):
    citas = []
    if Cita is not None:
        try:
            citas = list(Cita.objects.select_related().all()[:200])
        except Exception:
            citas = []
    if not citas:
        citas = [
            {'usuario': 'Carlos', 'psicologa': 'Dra. Ana Pérez', 'fecha': '2025-11-10 10:00', 'estado': 'Confirmada'},
            {'usuario': 'María', 'psicologa': 'Dra. Laura Gómez', 'fecha': '2025-11-12 15:30', 'estado': 'Pendiente'},
        ]
    return render(request, 'ui_frontend/citas_list.html', {'citas': citas})
