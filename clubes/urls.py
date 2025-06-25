from django.urls import path, include
from rest_framework import routers 
from .views import ClubViewSet,AdministradorClubViewSet, RegistroClubView

router_desc = routers.DefaultRouter()
router_desc.register(r'clubes', ClubViewSet, basename='clubes')
router_desc.register(r'administradores', AdministradorClubViewSet, basename='administradores')


urlpatterns = [
    path('api', include(router_desc.urls)),
    path('api/registro-club/', RegistroClubView.as_view(), name='registro-club')
]