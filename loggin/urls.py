# usuarios/urls.py

from django.urls import path
from .views import CustomLoginView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomLoginView, RefreshTokenFromCookieView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='custom_login'),
    path('api/token/refresh/', RefreshTokenFromCookieView.as_view(), name='token_refresh_cookie'),

]