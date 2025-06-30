from rest_framework import serializers
from .models import Atleta, AtletaDeporte
from deportes.models import Deporte
from django.contrib.auth import get_user_model
from .asignacion_de_categoria import determinar_categoria
from clubes.models import Club, ClubAtleta



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
    fecha_nacimiento = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    telefono = serializers.CharField()
    foto = serializers.ImageField(required=False, allow_null=True)
    descripcion = serializers.CharField(required=False, allow_blank=True)
    deporte_id = serializers.IntegerField()
    nivel_habilidad = serializers.ChoiceField(choices=AtletaDeporte.NIVELES)
    club_id = serializers.IntegerField()



    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value
    

    def create(self, validated_data):
        # Extraemos los datos del atleta
        deporte = Deporte.objects.get(id=validated_data['deporte_id'])
        nombre = validated_data.pop('nombre')
        apellido = validated_data.pop('apellido')
        fecha_nacimiento = validated_data.pop('fecha_nacimiento')
        telefono = validated_data.pop('telefono')
        descripcion = validated_data.pop('descripcion', '')
        foto = validated_data.pop('foto', None)
        categoria = determinar_categoria(
            deporte.nombre,
            fecha_nacimiento
        )


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
            categoria=categoria,  # Asignamos la categoría calculada
            foto_perfil=foto,  # Asignamos la foto si se proporciona
        )

        deporte = Deporte.objects.get(id=validated_data['deporte_id'])

        atletaDeporteVar = AtletaDeporte.objects.create(
            atleta=atleta,
            deporte=deporte,  # Inicialmente sin deporte asignado
            nivel_habilidad=validated_data['nivel_habilidad'],  # Inicialmente sin nivel de habilidad
        )
        
        club = Club.objects.get(id=validated_data['club_id'])

        
        atleta_inscripcion = ClubAtleta.objects.create(
            
            atleta = atleta,
            club  = club
            )

        return usuario
    

class ClubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Club
        fields = '__all__'



class ClubAtletaSerializer(serializers.Serializer):
    
    club = serializers.IntegerField()
    serial_club = serializers.CharField()
    
    
    def validate(self, data):
        request = self.context.get('request')
        atleta_id = request.COOKIES.get('id_atleta', None)
        club_id = data['club']

        # Validar que existan el atleta y el club
        if not Atleta.objects.filter(id=atleta_id).exists():
            raise serializers.ValidationError("El atleta no existe.")
        if not Club.objects.filter(id=club_id).exists():
            raise serializers.ValidationError("El club no existe.")

        # Validar que no tenga ya una inscripción activa
        if ClubAtleta.objects.filter(atleta_id=atleta_id, activo=True).exists():
            raise serializers.ValidationError("El atleta ya está inscrito activamente en otro club.")

        return data

    def create(self, validated_data):
        request = self.context.get('request')
        atleta_id = request.COOKIES.get('id_atleta', None)
        atleta = Atleta.objects.get(id=atleta_id)
        club = Club.objects.get(id=validated_data['club'])

        # Se usa la lógica de `save()` definida en el modelo
        inscripcion = ClubAtleta.objects.create(
            atleta=atleta,
            club=club,
            activo=True
        )
        return inscripcion
    






class InscripcionesSerializer(serializers.ModelSerializer):
    nombre_club = serializers.ReadOnlyField(source='club.nombre')
    nombre_atleta = serializers.ReadOnlyField(source='atleta.nombre')
    class Meta:
        model = ClubAtleta
        fields = ['id', 'fecha_registro', 'activo', 'fecha_baja', 'atleta', 'club', 'nombre_club', 'nombre_atleta']
