from rest_framework import routers
from actividad.views import actividad_serializer

routerr=routers.DefaultRouter()
routerr.register(r'activity/',actividad_serializer,'activity')