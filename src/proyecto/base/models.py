from django.db import models
from django.contrib.auth.models import User  # talba que probee django


# Create your models here.


class Tarea(models.Model):
    # Uno a muchos, cuando se elimine que pachara
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True,
                                blank=True)

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)  # Autocompletado de la pfecha de manera automatica

    def __str__(self):
        return self.titulo

    class Meta:
        # orden de las tareas
        ordering = ['completo']

    # Migracion - migrar nuestro modelo a la base de datos
