from rest_framework import serializers
from encuesta.models import encuesta

class encuesta_serializers(serializers.ModelSerializer):
    class Meta:
        model=encuesta
        fields='__all__'

