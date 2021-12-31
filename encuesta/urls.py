from django.urls import path,include
from encuesta.views import encuenstaview
from rest_framework import routers

router=routers.SimpleRouter()
router.register('survery',encuenstaview,basename='survery')

urlpatterns = [
    # API Webservices
    #path('propiedad/', views.PropiedadView.as_view()),
]
urlpatterns = router.urls + urlpatterns