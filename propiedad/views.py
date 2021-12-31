
from rest_framework.response import Response
from rest_framework import status,viewsets
from propiedad.models import propiedad
from propiedad.serializer import Propiedad_serializers
from propiedad.models import propiedad

# Create your views here.

class propiedad_views(viewsets.ModelViewSet):
    serializer_class=Propiedad_serializers
    queryset=propiedad.objects.all()
    authentication_classes = []
    permission_classes = []




