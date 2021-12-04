# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Libro(models.Model):

    titulo = models.CharField(max_length=13)
    paginas = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(70)])
    desc_corta = models.CharField(max_length=200, default='Sin reseña', verbose_name='Descripcion corta')
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}-{self.titulo}'