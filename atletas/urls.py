from django.urls import path, include
from rest_framework import routers 
from .views import AtletaViewSet


router_desc = routers.DefaultRouter()
router_desc.register(r'', AtletaViewSet)



urlpatterns = [
    path('', include(router_desc.urls))
    ]