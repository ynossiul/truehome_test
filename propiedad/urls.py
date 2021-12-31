from django.urls import path,include
from propiedad.views import propiedad_views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('property',propiedad_views,basename='property')

urlpatterns = [
    # API Webservices
    #path('propiedad/', views.PropiedadView.as_view()),
]
urlpatterns = router.urls + urlpatterns