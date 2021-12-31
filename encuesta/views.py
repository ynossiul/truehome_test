from rest_framework import viewsets
from encuesta.models import encuesta
from encuesta.serializer import encuesta_serializers
# Create your views here.

class encuenstaview(viewsets.ModelViewSet):
    serializer_class= encuesta_serializers
    queryset=encuesta.objects.all()
    authentication_classes = []
    permission_classes = []
