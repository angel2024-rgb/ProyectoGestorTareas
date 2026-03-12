from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarea
from .serializers import TareaSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

class TareaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tareas = Tarea.objects.filter(usuario=request.user)
        serializer = TareaSerializer(tareas, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TareaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(usuario = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TareaDetalleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        serializer = TareaSerializer(tarea)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        serializer = TareaSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        serializer = TareaSerializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


def login_view(request):
    return render(request, "tareas/login.html")

def registro_view(request):
    return render(request, "tareas/registro.html")

def dashboard_view(request):
    return render(request, "tareas/dashboard.html")