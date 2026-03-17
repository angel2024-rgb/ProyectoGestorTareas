from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categorías')

    def __str__(self):
        return self.nombre
