from django.db import models
from django.db.models.fields import CharField, DateTimeField
#from django.db.models.deletion import CASCADE
from propiedad.models import propiedad

# Create your models here.

class actividad(models.Model):
    Activo='Activo'
    Cancelado='Cancelado'
    Realizado='Realizado'
    Desactivada='Desactivada'

    status=[(Activo,'Activo'),(Cancelado,'Cancelada'),(Realizado,'Realizada')]
    property=models.ForeignKey(propiedad,on_delete=models.CASCADE)
    schedule=models.DateTimeField(auto_now_add=False)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=35,choices=status,default=Activo)

    def __str__(self):
        return self.title
