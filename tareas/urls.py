from django.urls import path
from .views import TareaView, TareaDetalleView, RegistroView, UsuarioView

urlpatterns = [
    path('tareas/', TareaView.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaDetalleView.as_view(), name='tarea-detail'),
    path('registro/', RegistroView.as_view(), name='registro-create'),
    path('usuarios/', UsuarioView.as_view(), name='usuario-list'),
]