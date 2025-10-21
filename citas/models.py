from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class ModalidadChoices(models.TextChoices):
    PRESENCIAL = 'presencial', 'Presencial'
    VIRTUAL = 'virtual', 'Virtual'
    TELEFONICA = 'telefonica', 'Telefónica'

class TipoCitaChoices(models.TextChoices):
    ORIENTACION = 'orientacion', 'Orientación'
    SEGUIMIENTO = 'seguimiento', 'Seguimiento'
    URGENCIA = 'urgencia', 'Urgencia'

class Cita(models.Model):
    estudiante = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='citas')
    psicologa = models.ForeignKey('psicologas.PerfilPsicologa', on_delete=models.CASCADE, related_name='citas')
    tipo = models.CharField(max_length=30, choices=TipoCitaChoices.choices, default=TipoCitaChoices.ORIENTACION)
    modalidad = models.CharField(max_length=30, choices=ModalidadChoices.choices, default=ModalidadChoices.PRESENCIAL)
    fecha_hora = models.DateTimeField()
    duracion_minutos = models.PositiveIntegerField(default=45, validators=[MinValueValidator(15), MaxValueValidator(240)])
    motivo = models.TextField(blank=True)
    aceptada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_hora']
        unique_together = ('psicologa','fecha_hora')

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.fecha_hora < timezone.now():
            raise ValidationError("No se puede agendar una cita en el pasado.")
    def __str__(self):
        return f"Cita {self.estudiante} con {self.psicologa} - {self.fecha_hora}"
