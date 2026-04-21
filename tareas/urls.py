from django.urls import path
from .views import TareaView, TareaDetalleView, RegistroView, UsuarioView, IAView

urlpatterns = [
    path('tareas/', TareaView.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaDetalleView.as_view(), name='tarea-detail'),
    path('registro/', RegistroView.as_view(), name='registro-create'),
    path('usuarios/', UsuarioView.as_view(), name='usuario-list'),
    path('IA/<int:pk>/', IAView.as_view(), name='IA-list'),
]