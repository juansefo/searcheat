from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receta(models.Model):
    nombre=models.CharField(max_length = 140)
    url=models.URLField()

    def __unicode__(self):
        return self.nombre