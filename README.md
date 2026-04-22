🇺🇸 English | 🇵🇪 [Versión en español](#español)

# Informational Portal with Task Manager

A web application combining personal task management with real-time weather and news from Lima. Built with Django REST Framework and JWT authentication, it now includes AI-powered subtask generation using RAG (Retrieval-Augmented Generation) with Google Gemini, ChromaDB vector database, and multilingual sentence-transformers.

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

### Generate list of subtasks using AI
![Subtasks](screenshots/listaSubtareas.png)

---

## Features

- **Real-time weather**: displays current temperature in Lima (external API).
- **Dynamic news feed**: scrollable list of headlines, dates, and descriptions.
- **Full CRUD** for tasks and categories (Create, Read, Update, Delete)
- **JWT Authentication** (Access and Refresh tokens)
- **Filters** by task status (All / Pending / Completed / Overdue) and by category
- **Responsive interface** built with vanilla HTML/CSS/JavaScript
- **Automatic token refresh**
- **AI-powered subtask generation**: automatic creation of subtasks using Google Gemini LLM.
- **RAG (Retrieval-Augmented Generation)**: enhance subtasks with content from external URLs, using semantic search with ChromaDB and multilingual embeddings.


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

### AI & RAG Pipeline
- **Google Gemini 2.5 Flash Lite** — LLM for subtask generation (free tier, 10 requests/day)
- **ChromaDB** — Persistent vector database for semantic search
- **Sentence-Transformers** — Multilingual embeddings (`paraphrase-multilingual-MiniLM-L12-v2`)
- **LangChain Community** — Web scraping and text splitting (WebBaseLoader, RecursiveCharacterTextSplitter)


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

### AI & RAG

The application uses **Retrieval-Augmented Generation (RAG)** to generate intelligent subtasks:

1. **URL Processing**: Accepts an external URL related to the task.
2. **Content Extraction**: Scrapes and cleans the webpage content.
3. **Semantic Search**: Splits text into chunks and generates embeddings using a multilingual model.
4. **Context Retrieval**: Finds the most relevant chunks based on the task description.
5. **Subtask Generation**: Sends the context to Google Gemini to produce actionable subtasks.

**Components used**:
- **Vector Database**: ChromaDB (persistent storage)
- **Embeddings**: `paraphrase-multilingual-MiniLM-L12-v2` (supports Spanish and English)
- **LLM**: Google Gemini 2.5 Flash Lite

⚠️ **Note**: To use the AI subtask feature you need a Google GenAI API key.
- Sign up at [Google AI Studio](https://aistudio.google.com/).
- Get your API key.
- Add it to your `.env` file: GEMINI_API_KEY="your_api_key"

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

## AI-Powered Subtask Generation

You can automatically generate a list of subtasks for each task using AI. After clicking the “IA” button, there are two options:

### Basic mode (no URL)
Click “Generar nuevas subtareas” button. The large language model (LLM) will create a logical breakdown based solely on the task description.

### RAG mode (with URL)
1. Provide a relevant URL.
2. Click "Generate new subtasks".
3. The system will:
   - Scrape and process the URL content
   - Find semantically relevant fragments
   - Generate context-aware subtasks using Gemini

**Example**:
- Task: *"Learn to drive a car"*
- URL: `http://chery.com.pe/blog/como-aprender-a-manejar-carro` 
> 💡 **Tip**: For best results, use URLs from blogs, documentation, or news articles that do not require JavaScript rendering (e.g., MDN, Django docs, university sites).
- Result: Detailed subtasks including legal requirements, vehicle familiarization, practice phases, and maintenance tips.

---

## Status
✅ Core task management (CRUD, filters, JWT auth)  
✅ Weather and news integration  
✅ AI subtask generation (basic + RAG with external URLs)  

---

<a name="español"></a>

🇺🇸 [English](#informational-portal-with-task-manager) | 🇵🇪 Versión en español

# Portal Informativo con Gestor de Tareas

Aplicación web que combina la gestión de tareas personales con el clima y las noticias de Lima en tiempo real. Construida con Django REST Framework y autenticación JWT, ahora incluye generación de subtareas con IA mediante RAG (Retrieval-Augmented Generation) con Google Gemini, la base de datos vectorial ChromaDB y embeddings multilingües de sentence-transformers.

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

### Generar lista de subtareas con IA
![Subtareas](screenshots/listaSubtareas.png)

---

## Características

-  **Clima en tiempo real**: muestra la temperatura actual en Lima (API externa).
-  **Lista dinámica de noticias**: lista de titulares, fechas y descripciones con scroll.
-  **CRUD completo** de tareas y categorías (Crear, Leer, Actualizar, Eliminar)
-  **Autenticación JWT** (Access y Refresh tokens)
-  **Filtros** por estado de tarea (Todas/Pendientes/Completadas/Atrasadas) y por categoría
-  **Interfaz responsive** con HTML/CSS/JavaScript vanilla
-  **Refresco automático** de tokens
- **Generación de subtareas con IA**: creación automática de subtareas usando Google Gemini LLM.
- **RAG (Retrieval-Augmented Generation)**: enriquece subtareas con contenido de URLs externas, usando búsqueda semántica con ChromaDB y embeddings multilingües.


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

### Pipeline de IA y RAG
- **Google Gemini 2.5 Flash Lite** — LLM para generación de subtareas (plan gratuito, 10 peticiones/día)
- **ChromaDB** — Base de datos vectorial persistente para búsqueda semántica
- **Sentence-Transformers** — Embeddings multilingües (`paraphrase-multilingual-MiniLM-L12-v2`)
- **LangChain Community** — Web scraping y división de texto (WebBaseLoader, RecursiveCharacterTextSplitter)

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

### IA y RAG

La aplicación utiliza **Retrieval-Augmented Generation (RAG)** para generar subtareas inteligentes:

1. **Procesamiento de URL**: Acepta una URL externa relacionada con la tarea.
2. **Extracción de contenido**: Extrae y limpia el contenido de la página web.
3. **Búsqueda semántica**: Divide el texto en fragmentos y genera embeddings con un modelo multilingüe.
4. **Recuperación de contexto**: Encuentra los fragmentos más relevantes según la descripción de la tarea.
5. **Generación de subtareas**: Envía el contexto a Google Gemini para producir subtareas accionables.

**Componentes utilizados**:
- **Base de datos vectorial**: ChromaDB (almacenamiento persistente)
- **Embeddings**: `paraphrase-multilingual-MiniLM-L12-v2` (soporta español e inglés)
- **LLM**: Google Gemini 2.5 Flash Lite

⚠️ **Nota**: Para usar la función de subtareas con IA necesitas una API key de Google GenAI.
- Regístrate en [Google AI Studio](https://aistudio.google.com/).
- Obtén tu API key.
- Agrégala a tu archivo `.env`: GEMINI_API_KEY="tu_clave_api"

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

## Generación de subtareas usando IA

Puedes generar automáticamente una lista de subtareas para cada tarea mediante IA. Tras hacer clic en el botón "IA", hay dos opciones:

### Modo básico (sin URL)
Haz clic en el botón «Generar nuevas subtareas». El modelo de lenguaje grande (LLM) creará un desglose lógico basándose únicamente en la descripción de la tarea.

### Modo RAG (con URL)
1. Introduzca una URL relevante.
2. Haga clic en «Generar nuevas subtareas».
3. El sistema:
   - Extraerá y procesará el contenido de la URL
   - Encontrará fragmentos semánticamente relevantes
   - Generará subtareas contextuales utilizando Gemini

**Ejemplo**:
- Tarea: *«Aprender a conducir un coche»*
- URL: `http://chery.com.pe/blog/como-aprender-a-manejar-carro` 
> 💡 **Consejo**: Para obtener los mejores resultados, utiliza direcciones URL de blogs, documentación o artículos de noticias que no requieran la ejecución de JavaScript (por ejemplo, MDN, la documentación de Django o sitios web de universidades).
- Resultado: Subtareas detalladas que incluyen requisitos legales, familiarización con el vehículo, fases de práctica y consejos de mantenimiento.

---

## Estado
✅ Gestor de tareas (CRUD, filtros, autenticación JWT)  
✅ Integración de clima y noticias  
✅ Generación de subtareas con IA (básico + RAG con URLs externas)  