from django.urls import path, include
from rest_framework import routers 
from .views import AtletaViewSet, AtletaDeporteViewSet, RegistroAtletaView,AtletaxDeporte, PerfilAtletaView, RegisterClubView, VerificarInscripcionView


router_desc = routers.DefaultRouter()
router_desc.register(r'atleta', AtletaViewSet)
router_desc.register(r'atldpt', AtletaDeporteViewSet)

urlpatterns = [
    path('api', include(router_desc.urls)),
    path('api/registro/', RegistroAtletaView.as_view(), name='registro-atleta'),
    path('api/deportes/', AtletaxDeporte.as_view(), name='atletaxdeport'),
    path('api/perfil/', PerfilAtletaView.as_view(), name='perfil-atleta'),
    path('api/inscripcion/', RegisterClubView.as_view(), name='incriopcion-atleta'),
    path('api/verificar/inscripcion', VerificarInscripcionView.as_view(), name='incriopcion-verificar'),
]