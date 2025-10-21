from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True,
        validators=[RegexValidator(r'^\+?\d{7,15}$', 'Número de teléfono inválido')])
    es_psicologa = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username
