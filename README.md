# Portal Informativo con Gestor de Tareas

Una aplicación que combina gestión de tareas personales con información en tiempo real de clima y noticias de Lima, construida con Django REST Framework y JWT para autenticación.

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


## Características

-  **Clima en tiempo real**: muestra la temperatura actual en Lima (API externa).
-  **Lista dinámica de noticias**: lista de titulares, fechas y descripciones con scroll.
-  **CRUD completo** de tareas y categorías (Crear, Leer, Actualizar, Eliminar)
-  **Autenticación JWT** (Access y Refresh tokens)
-  **Filtros** por estado de tarea (Todas/Pendientes/Completadas/Atrasadas) y por categoría
-  **Interfaz responsive** con HTML/CSS/JavaScript vanilla
-  **Refresco automático** de tokens

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

## Dependencias
- Python: ver `requirements.txt`
- JavaScript: Axios (si se usa npm, ver `package.json`)

## Fuentes de datos / APIs externas

La aplicación consume información en tiempo real desde:

- **Clima**: API de [Open-Meteo](https://open-meteo.com/) para obtener la temperatura actual en Lima.
- **Noticias**: API gratuita de [NewsAPI](https://newsapi.org/) (versión limitada) para mostrar titulares y descripciones de Lima, recientes.
  ⚠️ **Nota**: Para usar esta funcionalidad (noticias) necesitas tu propio `API key`.  
  - Regístrate en [NewsAPI](https://newsapi.org/register).  
  - Obtén tu `API key`.  
  - Crea un archivo `.env` en la raíz del proyecto y define la variable de entorno:
      APITUBE_API_KEY="tu_api_key"
  - Luego asegúrate de que tu aplicación lea esta variable desde el entorno.  


## Instalación

### Requisitos previos
- Python 3.10+
- pip (gestor de paquetes)
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
   - Gestiona tus tareas: crear categorías, añadir tareas, filtrar por estado y categoría, editar y eliminar.

## Estado
Proyecto en desarrollo activo. Se aceptan sugerencias y mejoras.