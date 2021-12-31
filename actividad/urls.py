from django.urls import path,include
from actividad.views import Actividad_view
from rest_framework import routers

from actividad.views import Actividad_view,reagendar,cancelar


router=routers.SimpleRouter()
router.register('activity',Actividad_view,basename='activity')

urlpatterns = [
    # API Webservices
    path('reagendar/',reagendar.as_view()),
    path('cancelar/',cancelar.as_view())
]

urlpatterns = router.urls + urlpatterns