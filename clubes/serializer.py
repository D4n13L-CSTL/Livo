from rest_framework import serializers
from .models import Club, AdministradorClub


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class AdministradorClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorClub
        fields = '__all__'
