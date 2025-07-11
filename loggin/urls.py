# usuarios/urls.py

from django.urls import path
from .views import CustomLoginView, CheckAuthView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomLoginView, RefreshTokenFromCookieView, LogoutView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='custom_login'),
    path('logout', LogoutView.as_view(), name='LogoutView'),
    path('api/token/refresh/', RefreshTokenFromCookieView.as_view(), name='token_refresh'),
    path('api/check/', CheckAuthView.as_view(), name='check'),

]