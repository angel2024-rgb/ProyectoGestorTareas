from django.urls import path
from .views import CategoriaView, CategoriaDetalleView

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaDetalleView.as_view(), name='categoria-detail'),
]