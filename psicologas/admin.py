from django.contrib import admin
from .models import PerfilPsicologa, Especialidad, Disponibilidad

class DisponibilidadInline(admin.TabularInline):
    model = Disponibilidad
    extra = 1

@admin.register(PerfilPsicologa)
class PerfilPsicologaAdmin(admin.ModelAdmin):
    list_display = ('usuario','profesion','disponible')
    search_fields = ('usuario__username','usuario__first_name','usuario__last_name','profesion')
    list_filter = ('disponible',)
    inlines = [DisponibilidadInline]
    filter_horizontal = ('especialidades',)

admin.site.register(Especialidad)
