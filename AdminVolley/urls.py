"""
URL configuration for AdminVolley project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atletas/', include('atletas.urls')),
    path('calendario/', include('calendario.urls')),
    path('clubes/', include('clubes.urls')),
    path('core/', include('core.urls')),
    path('deportes/', include('deportes.urls')),
    path('membresias/', include('membresias.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('loggin/', include('loggin.urls')),  # Autenticación de DRF
    path('pagos/', include('gestion_pagos.urls')),  # Autenticación de DRF

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Documentación con Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Documentación con Redoc
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
