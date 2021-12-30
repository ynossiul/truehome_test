#from _typeshed import Self
from django.db import models
#from django.db.models.enums import Choices

# Create your models here.

class propiedad(models.Model):
    Activo='Activo'
    Cancelado='Desactivada'
    Realizado='Realizado'

    status=[(Activo,'Activo'),(Cancelado,'Desactivada'),(Realizado,'Realizada')]

    title=models.CharField(max_length=255,)
    address=models.CharField(),
    description=models.CharField(),
    created_at=models.DateTimeField(auto_now_add=True),
    update_at=models.DateTimeField(auto_now_add=True),
    disabled_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=35,choices=status,default=Activo)

    def __str__(self):
        return self.title
