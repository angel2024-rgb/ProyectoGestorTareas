from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
        
     