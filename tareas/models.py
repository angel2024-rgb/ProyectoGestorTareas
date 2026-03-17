from django.db import models
from django.contrib.auth.models import User
from categorías.models import Categoria

class Tarea(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categorias')
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False) 

    def __str__(self):
        return self.descripcion


    