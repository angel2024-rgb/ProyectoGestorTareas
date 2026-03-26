from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from django.conf import settings

class NoticiasView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        api_key = settings.APITUBE_API_KEY
        category = request.query_params.get("category.id", "medtop:13000000")
        location = request.query_params.get("location.name", "Lima")

        url = "https://api.apitube.io/v1/news/everything"
        params = {"category.id": category, "location.name": location, "api_key": api_key}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            noticias = [
                {
                    "title": n.get("title"),
                    "published_at": n.get("published_at"),
                    "description": n.get("description")
                }
                for n in data.get("results", [])
            ]
            return Response(noticias)
        else:
            return Response({
                "error": "No se pudieron obtener las noticias",
                "details": response.text
            }, status=response.status_code)