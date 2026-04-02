🇺🇸 English | 🇵🇪 [Versión en español](#español)

# Informational Portal with Task Manager

A web application combining personal task management with real-time weather and news 
information from Lima, built with Django REST Framework and JWT authentication.

---

## Demo

### Login Screen with Weather and News
![Login](screenshots/login.png)

### Register
![Register](screenshots/registro.png)

### Task List
![Task list and categories](screenshots/listaTareas.png)

### Add Category
![Add category](screenshots/añadirCategoría.png)

### Add Task
![Add task](screenshots/añadirTarea.png)

---

## Features

- **Real-time weather**: displays current temperature in Lima (external API).
- **Dynamic news feed**: scrollable list of headlines, dates, and descriptions.
- **Full CRUD** for tasks and categories (Create, Read, Update, Delete)
- **JWT Authentication** (Access and Refresh tokens)
- **Filters** by task status (All / Pending / Completed / Overdue) and by category
- **Responsive interface** built with vanilla HTML/CSS/JavaScript
- **Automatic token refresh**

---

## Tech Stack

### Backend
- **Django 6.0** — Web framework
- **Django REST Framework 3.16** — REST API
- **Simple JWT 5.5** — Token-based authentication
- **SQLite** — Database (development)

### Frontend
- **HTML5** — Structure
- **CSS3** — Styles
- **JavaScript (Vanilla)** — Client-side logic
- **Fetch API** — HTTP requests

---

## Dependencies
- Python: see `requirements.txt`
- JavaScript: Axios (if using npm, see `package.json`)

---

## External APIs

The application retrieves real-time data from:

- **Weather**: [Open-Meteo](https://open-meteo.com/) API for current temperature in Lima.
- **News**: [NewsAPI](https://newsapi.org/) free tier for recent Lima headlines and descriptions.

  ⚠️ **Note**: To use the news feature you need your own API key.
  - Sign up at [NewsAPI](https://newsapi.org/register).
  - Get your API key.
  - Create a `.env` file in the project root and define:
      APITUBE_API_KEY="your_api_key"
  - Make sure your application reads this variable from the environment.

---

## Installation

### Prerequisites
- Python 3.10+
- pip
- Git

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/angel2024-rgb/ProyectoGestorTareas.git
cd ProyectoGestorTareas

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

## How to Use

1. **Access the app**: http://127.0.0.1:8000/
2. **Register** or log in
3. **Explore the portal**:
   - View the current temperature.
   - Browse recent news with the scroll feed.
   - Manage your tasks: create categories, add tasks, filter by status and category, 
   edit and delete.

---

## Status
Actively under development. Suggestions and contributions are welcome.

---

<a name="español"></a>

🇺🇸 [English](#informational-portal-with-task-manager) | 🇵🇪 Versión en español

# Portal Informativo con Gestor de Tareas

Una aplicación que combina gestión de tareas personales con información en tiempo real 
de clima y noticias de Lima, construida con Django REST Framework y JWT para autenticación.

---

## Demo

### Pantalla de Login con Clima y Noticias
![Login](screenshots/login.png)

### Registro
![Registro](screenshots/registro.png)

### Lista de tareas
![Lista de tareas y categorías](screenshots/listaTareas.png)

### Añadir categoría
![Añadir categoría](screenshots/añadirCategoría.png)

### Añadir tarea
![Añadir tarea](screenshots/añadirTarea.png)

---

## Características

-  **Clima en tiempo real**: muestra la temperatura actual en Lima (API externa).
-  **Lista dinámica de noticias**: lista de titulares, fechas y descripciones con scroll.
-  **CRUD completo** de tareas y categorías (Crear, Leer, Actualizar, Eliminar)
-  **Autenticación JWT** (Access y Refresh tokens)
-  **Filtros** por estado de tarea (Todas/Pendientes/Completadas/Atrasadas) y por categoría
-  **Interfaz responsive** con HTML/CSS/JavaScript vanilla
-  **Refresco automático** de tokens

---

## Tecnologías utilizadas

### Backend
- **Django 6.0** - Framework web
- **Django REST Framework 3.16** - API REST
- **Simple JWT 5.5** - Autenticación por tokens
- **SQLite** - Base de datos (desarrollo)

### Frontend
- **HTML5** - Estructura
- **CSS3** - Estilos
- **JavaScript (Vanilla)** - Lógica de cliente
- **Fetch API** - Peticiones HTTP

---

## Dependencias
- Python: ver `requirements.txt`
- JavaScript: Axios (si se usa npm, ver `package.json`)

---

## Fuentes de datos / APIs externas

- **Clima**: API de [Open-Meteo](https://open-meteo.com/) para obtener la temperatura actual en Lima.
- **Noticias**: API gratuita de [NewsAPI](https://newsapi.org/) para mostrar titulares y descripciones de Lima, recientes.

  ⚠️ **Nota**: Para usar esta funcionalidad necesitas tu propio `API key`.
  - Regístrate en [NewsAPI](https://newsapi.org/register).
  - Obtén tu `API key`.
  - Crea un archivo `.env` en la raíz del proyecto y define:
      APITUBE_API_KEY="tu_api_key"
  - Luego asegúrate de que tu aplicación lea esta variable desde el entorno.

---

## Instalación

### Requisitos previos
- Python 3.10+
- pip
- Git

### Pasos de instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/angel2024-rgb/ProyectoGestorTareas.git
cd ProyectoGestorTareas

# 2. Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Realizar migraciones
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Ejecutar servidor
python manage.py runserver
```

## Cómo usar

1. **Accede a la aplicación**: http://127.0.0.1:8000/
2. **Regístrate** o inicia sesión
3. **Explora el portal**:
   - Visualiza la temperatura actual.
   - Consulta las noticias recientes con el scroll.
   - Gestiona tus tareas: crear categorías, añadir tareas, filtrar por estado y 
   categoría, editar y eliminar.

---

## Estado
Proyecto en desarrollo activo. Se aceptan sugerencias y mejoras.