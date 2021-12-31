from django.db import models
from actividad.models import actividad
# Create your models here.

class encuesta(models.Model):
    activity=models.OneToOneField(actividad,on_delete=models.CASCADE)
    answers=models.JSONField()
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return str(self.actividad.id) + '-' + self.actividad.title