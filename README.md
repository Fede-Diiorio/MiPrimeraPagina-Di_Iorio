# Blog de Warhammer 40.000

Este es un proyecto de blog básico con categorías, comentarios y gestión de usuarios desarrollado con Django. Permite:

- Crear, listar, editar y eliminar **blogs**
- Crear, listar, editar y eliminar **categorías**
- Registrar y gestionar **usuarios**
- Crear, editar o eliminar **comentarios** asociados a los **blogs**
- Buscar **blogs** por categoría y título

---

## 📦 Funcionalidades

- **Listado de blogs** con vista detallada por ID
- **Listado de blogs** creados por el usuario
- **Búsqueda de blogs** por nombre o **categoría**
- **Listado de categorias**
- **Visualización de comentario** con información de usuario y hora en la vista del detalle del blog
- **Registro e inicio de sesión de usuarios**, con perfil y creación de avatar
- Relación entre modelos: Cada blog está asociado a una categoría y a un usuario. Otros usuarios pueden crear comentarios asociados al blog.

---

## 🛠️ Tecnologías

- Python 3.x
- Django 5.2.3 – Framework principal del backend
- SQLite – Base de datos por defecto
- Pillow – Manejo de imágenes (por ejemplo, para avatares y entradas de blog)
- django-sass-processor – Compilación de SASS a CSS
- Black – Formateador de código Python
- Virtualenv – Entorno virtual para aislar dependencias

---

## ⚙️ Instalación y uso

1. Cloná este repositorio:

```bash
git clone https://github.com/Fede-Diiorio/MiPrimeraPagina-Di_Iorio.git
cd MiPrimeraPagina-Di_Iorio
```

2. Creá y activá un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutá migraciones y arrancá el servidor:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🎥 Demostración en video

**Link:** [Aquí](https://www.youtube.com/watch?v=Cuo3teMiNtc&ab_channel=Diyo292)

---

## 📄 Rutas importantes

### 📝 Blog

- `/blog/` → Lista de blogs
- `/blog/create/` → Crear un nuevo blog
- `/blog/<id>/` → Detalle de un blog
- `/blog/<id>/edit/` → Editar un blog
- `/blog/<id>/delete/` → Eliminar un blog
- `/blog/<id>/comment/` → Agregar comentario a un blog
- `/blog/<username>/` → Ver blogs por autor
- `/blog/search/` → Buscar blogs por título

---

### 💬 Comentarios

- `/comment/<id>/edit/` → Editar comentario
- `/comment/<id>/delete/` → Eliminar comentario

---

### 🗂️ Categorías

- `/categories/` → Lista de categorías
- `/categories/create/` → Crear nueva categoría
- `/category/<slug>/` → Ver blogs por categoría
- `/category/<id>/edit/` → Editar categoría
- `/category/<id>/delete/` → Eliminar categoría

---

### 👤 Cuentas de usuario

- `/register/` → Registro de usuario
- `/login/` → Iniciar sesión
- `/logout/` → Cerrar sesión
- `/update/` → Actualizar perfil
- `/profile/<username>/` → Ver perfil de usuario

---

### ℹ️ Otros

- `/about-me/` → Página "Sobre mí"
- `/` → Página principal (home)

---

## 🧩 Modelos

### Category

```python
name: CharField (máx 40)
slug: SlugField (único, máx 40)
image: TextField (URL de imagen, valor por defecto: "Sin-Imagen")
```

---

### Blog

```python
user: ForeignKey(User)
title: CharField (máx 70)
body: TextField
image: ImageField (upload_to="myapp/blog_images/")
date: DateField (auto_now_add=True)
is_active: BooleanField (default=True)
category: ForeignKey(Category)
```

---

### Comment

```python
user: ForeignKey(User)
blog: ForeignKey(Blog)
text: TextField
date: DateTimeField (auto_now_add=True)
```

---

### Avatar

```python
user: OneToOneField(User)
image: ImageField (upload_to="accounts/avatars")
```

---

## ✍️ Notas

- Las búsquedas utilizan `Q()` de Django para permitir filtrar por múltiples campos.
- Los formularios están hechos con HTML simple + clases Bootstrap para estilo básico.
- Los objetos se ordenan por fecha de creación usando campos como `date` o `date_created`.

---

## 🚀 Mejoras posibles a futuro

- Soporte para paginación
- Estilos personalizados en los formularios
- Permitir la edición de blogs solo al creador
- Medidas de seguridad adicionales para convertirse en administrador

---
