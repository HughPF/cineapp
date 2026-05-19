# 🎬 CineApp - Catálogo de Películas

Aplicación web desarrollada con **Django 5** para la gestión colaborativa de un catálogo de películas. Cada usuario registrado puede añadir sus propias películas y consultar las de otros usuarios.

> **Proyecto académico** — Prueba de Evaluación 2 (Parte 2), módulo *Programación en Python* (2º DAW), curso 2025/2026.

---

## 🌐 Demo en línea

🔗 **https://hugoperezfermoso.pythonanywhere.com/**

| Usuario | Contraseña |
|---------|------------|
| `admin` | `admin1234` |
| `alvaro` | `cineapp123` |
| `maria` | `cineapp123` |

---

## 📋 Tabla de contenidos

1. [Características](#-características)
2. [Tecnologías utilizadas](#-tecnologías-utilizadas)
3. [Estructura del proyecto](#-estructura-del-proyecto)
4. [Instalación y puesta en marcha](#-instalación-y-puesta-en-marcha)
5. [Datos de ejemplo](#-datos-de-ejemplo)
6. [Funcionalidades obligatorias](#-funcionalidades-obligatorias)
7. [Funcionalidades adicionales](#-funcionalidades-adicionales)
8. [Autor](#-autor)

---

## ✨ Características

- **Catálogo público** de películas con paginación.
- **Buscador y filtro** por título, director, sinopsis y género.
- **Sistema completo de autenticación**: registro, login y logout.
- **Gestión CRUD** de películas (crear, ver, editar, eliminar) usando vistas basadas en clases.
- **Subida de carteles** (imágenes) para cada película.
- **Permisos granulares**: cada usuario solo puede editar sus propias películas; el personal staff/superusuario puede gestionar cualquier contenido.
- **Mensajes de feedback** mediante el framework Django Messages.
- **Diseño 100 % personalizado** con CSS propio responsive (sin frameworks externos).

---

## 🛠 Tecnologías utilizadas

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | 3.14+ | Lenguaje principal |
| Django | 5.2 | Framework web |
| Pillow | 12.x | Procesamiento de imágenes (ImageField) |
| CSS3 | — | Hoja de estilos personalizada (variables, grid, flexbox, media queries) |
| SQLite | 3 | Base de datos (desarrollo) |

---

## 📂 Estructura del proyecto

```
cineapp_project/
├── cineapp/                # Configuración del proyecto Django
│   ├── settings.py         # Configuración (BD, static, media, etc.)
│   ├── urls.py             # URLs raíz
│   └── wsgi.py
├── peliculas/              # App principal
│   ├── models.py           # Genero, Pelicula
│   ├── views.py            # Vistas basadas en clases (CBV)
│   ├── forms.py            # Formularios (Pelicula, Registro)
│   ├── urls.py             # URLs con name=
│   ├── admin.py            # Registro en panel de administración
│   └── migrations/
├── templates/              # Plantillas con herencia
│   ├── base.html           # Plantilla base con navbar dinámica
│   ├── peliculas/          # CRUD de películas
│   └── registration/       # login.html y registro.html
├── static/
│   └── css/estilos.css     # CSS personalizado (sin frameworks)
├── media/                  # Imágenes subidas (carteles)
├── manage.py
├── cargar_datos.py         # Script para cargar datos de ejemplo
├── requirements.txt
└── README.md
```

---

## 🚀 Instalación y puesta en marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/HughPF/cineapp.git
cd cineapp_project
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. (Opcional) Cargar datos de ejemplo
Crea automáticamente un superusuario, usuarios de prueba, géneros y películas:
```bash
python cargar_datos.py
```

### 6. Crear un superusuario manualmente (si no usas el script anterior)
```bash
python manage.py createsuperuser
```

### 7. Arrancar el servidor de desarrollo
```bash
python manage.py runserver
```

Accede a 👉 **http://127.0.0.1:8000/**

---

## 🔑 Datos de ejemplo

Si ejecutaste `cargar_datos.py`, dispones de los siguientes usuarios:

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `admin` | `admin1234` | Superusuario |
| `alvaro` | `cineapp123` | Usuario normal |
| `maria` | `cineapp123` | Usuario normal |

Y 8 películas precargadas con géneros y autores variados.

---

## ✅ Funcionalidades obligatorias

### Estructura y entorno
- [x] Entorno virtual (`venv/`)
- [x] `requirements.txt` con todas las dependencias
- [x] Historial de commits Git con mensajes descriptivos

### Modelo de datos
- [x] Modelo `Pelicula` con:
  - `titulo` — campo de texto corto (`CharField`)
  - `sinopsis` — campo de texto largo (`TextField`)
  - `fecha_creacion` — fecha automática (`auto_now_add=True`)
  - `autor` — `ForeignKey` al modelo `User` de Django

### Lógica de negocio y URLs
- [x] **Vistas basadas en clases (CBV)**: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`.
- [x] **CRUD completo**: listar, ver detalle, añadir, editar y eliminar películas.
- [x] **URLs con `name`** para todas las rutas (uso de `reverse_lazy` y `{% url %}`).

### Interfaz y plantillas
- [x] Herencia de plantillas con `base.html` y bloques `{% block %}`.
- [x] Directorio `static/` a nivel de proyecto con CSS propio.
- [x] **Navbar dinámica**: muestra opciones diferentes según el usuario esté autenticado o no.

### Usuarios y seguridad
- [x] Login, Logout y Registro (Sign Up) implementados.
- [x] `LoginRequiredMixin` en todas las vistas de creación, edición y borrado.
- [x] **Mixin personalizado `StaffOrAuthorMixin`** (`UserPassesTestMixin`): solo el autor o un usuario staff/superusuario puede editar/borrar el contenido.
- [x] Mensajes de error mediante el framework `django.contrib.messages` (con tags personalizados).
- [x] Excepción de staff/superusuario para gestionar cualquier contenido del sitio.

### Despliegue
- [x] Aplicación desplegada en https://www.pythonanywhere.com/ *(URL en la documentación PDF)*.

---

## 🌟 Funcionalidades adicionales

Se han implementado **3 funcionalidades adicionales**:

### 1. Gestión de imágenes (carteles)
- Cada película puede tener un cartel asociado mediante un campo `ImageField`.
- Configuración de `MEDIA_URL` y `MEDIA_ROOT` en `settings.py`.
- Los formularios usan `enctype="multipart/form-data"`.
- Si una película no tiene cartel se muestra un placeholder con icono.
- Las imágenes se guardan en `media/carteles/` y se sirven en desarrollo mediante `static()`.

### 2. Búsqueda y filtrado
- Barra de búsqueda en el catálogo.
- Filtro por género (desplegable).
- Implementado con `Q` objects para buscar simultáneamente en `titulo`, `director` y `sinopsis`.
- Combinable con paginación (los parámetros se preservan al cambiar de página).

### 3. Ampliación del modelo (modelo `Genero`)
- Nuevo modelo `Genero` con relación `ForeignKey` desde `Pelicula` (`on_delete=SET_NULL`).
- Permite categorizar películas y filtrar por género.
- Gestionable desde el panel admin (`/admin/`).
- Accesible desde el formulario de creación/edición de películas.


---

## 👤 Autor

Desarrollado por: **Hugo Pérez Fermoso**
- 🎓 Ciclo: 2º DAW
- 📚 Módulo: Programación en Python
- 📅 Curso: 2025/2026
- 👨‍🏫 Profesor: Álvaro García

---

## 📜 Licencia

Proyecto académico realizado con fines educativos.
