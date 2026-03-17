from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class CategoriaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categorias = Categoria.objects.filter(usuario=request.user)
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoriaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(usuario = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetalleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk, usuario=request.user)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk, usuario=request.user)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk, usuario=request.user)
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk, usuario=request.user)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
