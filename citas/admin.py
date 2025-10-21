from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id','estudiante','psicologa','tipo','modalidad','fecha_hora','aceptada')
    list_filter = ('tipo','modalidad','aceptada')
    search_fields = ('motivo','estudiante__username','psicologa__usuario__username')
    date_hierarchy = 'fecha_hora'
