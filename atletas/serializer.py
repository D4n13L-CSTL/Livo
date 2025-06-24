from rest_framework import serializers
from .models import Atleta, AtletaDeporte
from deportes.models import Deporte
from django.contrib.auth import get_user_model

Usuario = get_user_model()




class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'
        
class AtletaDeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtletaDeporte
        fields = '__all__'
    
 



class RegistroAtletaSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    fecha_nacimiento = serializers.DateField()
    telefono = serializers.CharField()
    foto = serializers.ImageField(required=False, allow_null=True)
    descripcion = serializers.CharField(required=False, allow_blank=True)
    deporte_id = serializers.IntegerField()
    nivel_habilidad = serializers.ChoiceField(choices=AtletaDeporte.NIVELES)

    def create(self, validated_data):
        # Extraemos los datos del atleta
        nombre = validated_data.pop('nombre')
        apellido = validated_data.pop('apellido')
        fecha_nacimiento = validated_data.pop('fecha_nacimiento')
        telefono = validated_data.pop('telefono')
        descripcion = validated_data.pop('descripcion', '')
        foto = validated_data.pop('foto', None)

        # Creamos el usuario
        usuario = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            tipo_usuario='ATLETA',
            username=validated_data['email'],  # si usas email como username
            telefono=telefono
        )

        # Creamos el perfil de atleta vinculado
        atleta = Atleta.objects.create(
            usuario=usuario,
            email = validated_data['email'],
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            descripcion=descripcion,
            foto_perfil=foto,  # Asignamos la foto si se proporciona
        )

        deporte = Deporte.objects.get(id=validated_data['deporte_id'])

        atletaDeporteVar = AtletaDeporte.objects.create(
            atleta=atleta,
            deporte=deporte,  # Inicialmente sin deporte asignado
            nivel_habilidad=validated_data['nivel_habilidad'],  # Inicialmente sin nivel de habilidad
        )

        return usuario