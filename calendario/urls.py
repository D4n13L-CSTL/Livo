from django.urls import path, include
from rest_framework import routers 
from .views import EventoCalendarioViewSet

routers_api = routers.DefaultRouter()
routers_api.register(r'eventos', EventoCalendarioViewSet)


urlpatterns = [
    path('api', include(routers_api.urls))
    ]