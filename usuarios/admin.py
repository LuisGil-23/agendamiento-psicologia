from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','es_psicologa','is_active')
    list_filter = ('es_psicologa','is_staff','is_superuser','is_active')
    search_fields = ('username','email','first_name','last_name')
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Información personal', {'fields': ('first_name','last_name','email','telefono','es_psicologa')}),
        ('Permisos', {'fields': ('is_active','is_staff','is_superuser','groups')}),
        ('Fechas importantes', {'fields': ('last_login','date_joined')}),
    )
