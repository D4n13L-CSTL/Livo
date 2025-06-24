from django.urls import path, include
from rest_framework import routers 
from .views import AtletaViewSet, AtletaDeporteViewSet, RegistroAtletaView


router_desc = routers.DefaultRouter()
router_desc.register(r'atleta', AtletaViewSet)
router_desc.register(r'atldpt', AtletaDeporteViewSet)



urlpatterns = [
    path('api', include(router_desc.urls)),
    path('api/registro/', RegistroAtletaView.as_view(), name='registro-atleta')
]