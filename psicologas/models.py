from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    def __str__(self): return self.nombre

class PerfilPsicologa(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_psicologa')
    profesion = models.CharField(max_length=200)
    resumen = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='psicologas/', blank=True, null=True)
    especialidades = models.ManyToManyField(Especialidad, blank=True)
    duracion_minutos_default = models.PositiveIntegerField(default=45, validators=[MinValueValidator(15), MaxValueValidator(240)])
    disponible = models.BooleanField(default=True)
    def __str__(self): return f"{self.usuario.get_full_name()} - {self.profesion}"

class Disponibilidad(models.Model):
    psicologa = models.ForeignKey(PerfilPsicologa, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.IntegerField(choices=[(i, d) for i, d in enumerate(['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'])])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    class Meta:
        unique_together = ('psicologa','dia_semana','hora_inicio','hora_fin')
    def __str__(self): return f"{self.psicologa} - {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"
