from django.urls import path, include
from rest_framework import routers 


router_desc = routers.DefaultRouter()



urlpatterns = [
    path('api', include(router_desc.urls))
    ]