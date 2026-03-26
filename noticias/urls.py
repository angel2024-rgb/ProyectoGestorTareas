from django.urls import path
from .views import NoticiasView

urlpatterns = [
    path("noticias/", NoticiasView.as_view(), name="noticias"),
]