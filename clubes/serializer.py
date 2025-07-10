from rest_framework import serializers
from .models import Club, AdministradorClub, ClubAtleta
from django.contrib.auth import get_user_model
from deportes.models import Deporte

Usuario = get_user_model()

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class AdministradorClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorClub
        fields = '__all__'



class RegistroClubSerializer(serializers.Serializer):
    nombre_club = serializers.CharField()
    nombre_encargado = serializers.CharField()
    usuario_club = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    telefono = serializers.CharField()
    logo = serializers.ImageField(required=False, allow_null=True)
    descripcion = serializers.CharField(required=False, allow_blank=True)
    deporte_id = serializers.IntegerField()
    direccion_club = serializers.CharField(required=False, allow_blank=True)
    

    """def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value"""
    

    def create(self, validated_data):
        # Extraemos los datos del club
        nombre_club = validated_data.pop('nombre_club')
        nombre_encargado = validated_data.pop('nombre_encargado')
        telefono = validated_data.pop('telefono')
        descripcion = validated_data.pop('descripcion', '')
        direccion_club = validated_data.pop('direccion_club', '')
        logo = validated_data.pop('logo', None)


        # Creamos el usuario
        usuario = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            tipo_usuario='CLUB',
            username=validated_data['usuario_club'].upper() # si usas email como username
        )

        # Creamos el perfil de atleta vinculado
        club = Club.objects.create(
            nombre = nombre_club,
            direccion_club=direccion_club,
            logo=logo,
            deporte=Deporte.objects.get(id=validated_data['deporte_id']),
            año_fundacion=2023,  # Puedes ajustar esto según tus necesidades
            ubicacion=validated_data.get('ubicacion', ''),
            descripcion=descripcion,
            )

        AdministradorClub.objects.create(           
            email=validated_data['email'],
            nombre_completo=nombre_encargado,
            telefono=telefono,
            club=club,
            usuario=usuario
        )

    
        return usuario
    




class VerAtletasRegister(serializers.ModelSerializer):
    
    nombre_atleta= serializers.ReadOnlyField(source='atleta.nombre')
    class Meta:
        model = ClubAtleta
        fields = ['id','nombre_atleta']

#COMENZANDO SERIALIZADOR PARA DATOS DE ESTUDIANTES DEL CLUB

