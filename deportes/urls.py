from django.urls import path, include
from rest_framework import routers 
from .views import DeporteViewSet

router_desc = routers.DefaultRouter()
router_desc.register(r'deportes', DeporteViewSet, basename='deportes')

urlpatterns = [
    path('api', include(router_desc.urls))
    ]