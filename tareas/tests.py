from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase


class BaseAPITestCase(APITestCase):
    def setUp(self):
        # Cliente de pruebas
        self.client = APIClient()
        # Crear usuario de prueba
        self.user = User.objects.create_user(username="tester", password="123456")

        # Obtener token JWT
        response = self.client.post("/api/token/", {
            "username": "tester",
            "password": "123456"
        }, format="json")

        self.token = response.data["access"]
        # Configurar autenticación en el cliente
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")


class TareaViewTest(BaseAPITestCase):
    def test_list_tareas(self):
        url = reverse("tarea-list-create")
        self.client.post(url, {"descripcion": "Tarea1", "fecha_fin": "2026-03-13"}, format="json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_tarea(self):
        url = reverse("tarea-list-create") 
        response = self.client.post(url, {"descripcion": "Tarea1", "fecha_fin": "2026-03-13"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["descripcion"], "Tarea1")
        self.assertEqual(response.data["fecha_fin"], "2026-03-13")


""" class TaskTests(BaseAPITestCase):
    def test_create_task(self):
        url = reverse("tarea-list-create")  # nombre de ruta del router
        response = self.client.post(url, {"title": "Nueva tarea"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Nueva tarea")

    def test_list_tasks(self):
        url = reverse("task-list")
        self.client.post(url, {"title": "Tarea 1"}, format="json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_task(self):
        url = reverse("task-list")
        task = self.client.post(url, {"title": "Detalle"}, format="json").data
        detail_url = reverse("task-detail", args=[task["id"]])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Detalle")

    def test_update_task(self):
        url = reverse("task-list")
        task = self.client.post(url, {"title": "Viejo título"}, format="json").data
        detail_url = reverse("task-detail", args=[task["id"]])
        response = self.client.patch(detail_url, {"title": "Nuevo título"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Nuevo título")

    def test_delete_task(self):
        url = reverse("task-list")
        task = self.client.post(url, {"title": "Eliminar"}, format="json").data
        detail_url = reverse("task-detail", args=[task["id"]])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, 204) """
