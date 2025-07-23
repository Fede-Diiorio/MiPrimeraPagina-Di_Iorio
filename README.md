# Blog de Warhammer 40.000 — Proyecto Django

Este es un proyecto de gestión básica de productos, clientes y órdenes desarrollado con Django. Permite:
Este es un proyecto básico de blog, con categorias, comentarios y registro de usuarios. Permite:

- Crear, listar y buscar **blogs**
- Crear y manejar **usuarios**
- Registrar **comentarios** asociadas a los usuarios en los **blogs**
- Buscar **blogs** según la categoría en la que estén registrados y por su nombre

---

## 📦 Funcionalidades

- **Listado de blogs** con vista detallada por ID
- **Listado de blogs** creados por el usuarioj
- **Búsqueda de blogs** por nombre o **categoría**
- **Listado de categorias**
- **Visualización de comentario** con información de usuario y hora en la vista del detalle del blog
- Registro e identificación **usuarios** con vista detallada incluyendo creación de avatar
- Relación entre modelos: Cada blog está asociado a una categoría y a un usuario. Otros usuarios pueden crear comentarios asociados al blog.

---

## 🛠️ Tecnologías

- Python 3.x
- Django
- HTML + Bootstrap (para estilos simples en las vistas)
- SQLite (por defecto)

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

## 📄 Rutas importantes

### 📝 Blog

- `/blog/` → Lista de blogs
- `/blog/create/` → Crear un nuevo blog
- `/blog/<id>/` → Detalle de un blog
- `/blog/<id>/edit/` → Editar un blog
- `/blog/<id>/delete/` → Eliminar un blog
- `/blog/<id>/comment/` → Agregar comentario a un blog
- `/blog/<username>/` → Ver blogs por autor
- `/blogs/search/` → Buscar blogs por título

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
image: TextField (URL de imagen, por defecto "Sin-Imagen")
```

---

### Blog

```python
user: ForeignKey(User)
title: CharField (máx 70)
body: TextField
image: ImageField (upload_to="myapp/blog_images/", default="myapp/blog_images/default.jpg")
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
- El campo `created_at` se usa en órdenes para mostrar cuándo fue creada cada orden.

---

## 🚀 Mejoras posibles a futuro

- Soporte para paginación

---
