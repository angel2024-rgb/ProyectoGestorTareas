from rest_framework import serializers
from .models import Tarea
from django.contrib.auth.models import User
import re
from datetime import date

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

        extra_kwargs = {
            'email': {'required': False},
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        value = value.strip()
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9_]+$', value):
            raise serializers.ValidationError("El nombre de usuario solo debe contener letras, números y guiones bajos")
        
        if len(value)<3:
            raise serializers.ValidationError("El nombre de usuario debe tener como mínimo 3 caracteres.")
        
        return value


    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("La contraseña es obligatoria.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class TareaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Tarea
        fields = '__all__'
        read_only_fields = ['fecha_inicio', 'usuario']

    def validate_descripcion(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError("La descripción debe tener al menos 3 caracteres.")
        return value
    
    def validate(self, data):
        if data.get('fecha_fin'):
            if data['fecha_fin'] < date.today():
                raise serializers.ValidationError("Fecha de fin incorrecta")
        return data
        
    