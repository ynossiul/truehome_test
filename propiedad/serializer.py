from django.db import models
from rest_framework import fields, serializers
from propiedad.models import propiedad

class Propiedad_serializers(serializers.ModelSerializer):
    class Meta:
        model=propiedad
        fields='__all__'
    
   
    