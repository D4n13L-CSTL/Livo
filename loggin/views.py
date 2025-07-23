from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from django.utils import timezone
from .serializer import CustomTokenObtainPairSerializer  # tu serializador
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.views import APIView
from atletas.models import Atleta
from rest_framework.permissions import IsAuthenticated
from middleware.jwt_cookie_auth import CustomJWTAuthentication




class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
    
        serializer.is_valid(raise_exception=True)
  

        access_token = serializer.validated_data['access']
        refresh_token = serializer.validated_data['refresh']
        response = Response({
            "tipo_usuario": serializer.validated_data['tipo_usuario'],
            "email": serializer.validated_data['email'],
            "username": serializer.validated_data['username']
        })

        # Configurar las cookies HttpOnly
        expires = timezone.now() + timedelta(days=1)
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=True,  # True en producción (HTTPS)
            samesite='None',
            expires=expires
        )

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='None',
            expires=expires + timedelta(days=7)  # o lo que dure el refresh
        )


        response.set_cookie(
        key='deporte',
        value=serializer.validated_data.get('deporte', ''),
        httponly=False,  # Si quieres acceder desde JS
        secure=True,
        samesite='None',
        expires=expires
    )
        
        response.set_cookie(
        key='id_deporte',
        value=serializer.validated_data.get('deporte_id', ''),
        httponly=False,  # Si quieres acceder desde JS
        secure=True,
        samesite='None',
        expires=expires
    )
        response.set_cookie(
        key='serial_club',
        value=serializer.validated_data.get('serial_club', 'sinSerial'),
        httponly=True,  # Si quieres acceder desde JS
        secure=True,
        samesite='None',
        expires=expires
    )
        

        return response
    




class RefreshTokenFromCookieView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token is None:
            return Response({"detail": "Refresh token no encontrado."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)

            response = Response({"detail": "Token refrescado correctamente."})

            # Establecer el nuevo token de acceso como cookie
            expires = timezone.now() + timedelta(days=1)
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                httponly=True,
                secure=True,
                samesite='Lax',
                expires=expires
            )

            return response

        except TokenError as e:
            return Response({"detail": "Token inválido o expirado."}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
    

class LogoutView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"detail": "Sesión cerrada correctamente."}, status=status.HTTP_200_OK)

        # Eliminar cookies
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        response.delete_cookie('deporte')
        response.delete_cookie('id_deporte')
        response.delete_cookie('serial_club')

        # Opcional: revocar el refresh token
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Necesitás tener configurado el blacklist
            except Exception:
                pass  # Si ya está expirado o no es válido, lo ignoramos

        return response


class CheckAuthView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'authenticated': True}, status=status.HTTP_200_OK)