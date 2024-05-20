from django.db import models

from accounts.models import RegisterUserModel


# Create your models here.
class LabelTodosModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Etiquetas'
        verbose_name = 'Etiqueta'

    def __str__(self):
        return self.name


class TodosUserModel(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en progreso', 'En progreso'),
        ('completada', 'Completada'),
    )

    user = models.ForeignKey(RegisterUserModel, on_delete=models.CASCADE, verbose_name='Nombre Usuario')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    observations = models.TextField(verbose_name='Observaciones', blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendiente', verbose_name='Estado')
    due_date = models.DateField(verbose_name='Fecha de Vencimiento')
    labels = models.ManyToManyField(LabelTodosModel, blank=True, verbose_name='Etiquetas')

    class Meta:
        verbose_name_plural = 'Tareas'
        verbose_name = 'Tarea'

    def __str__(self):
        return self.title
