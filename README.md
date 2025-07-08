# Inventario y Gestión de Productos — Proyecto Django

Este es un proyecto de gestión básica de productos, clientes y órdenes desarrollado con Django. Permite:

- Crear, listar y buscar **productos**
- Gestionar **clientes**
- Registrar **órdenes** asociadas a clientes
- Buscar tanto **clientes** como **órdenes** y **productos** mediante formularios

---

## 📦 Funcionalidades

- **Listado de productos** con vista detallada por ID
- **Búsqueda de productos** por nombre
- **Listado de clientes** y búsqueda por nombre o apellido
- **Visualización de órdenes** y búsqueda por nombre del cliente
- Relación entre modelos: cada orden pertenece a un cliente y contiene múltiples productos

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

- `/productos/` → Lista de productos
- `/productos/nuevo/` → Crear producto
- `/productos/buscar/` → Formulario de búsqueda de productos
- `/productos/<id>/` → Detalle del producto
- `/clientes/` → Lista de clientes
- `/clientes/nuevo/` → Crear cliente
- `/clientes/buscar/` → Buscar cliente por nombre o apellido
- `/ordenes/` → Lista de órdenes
- `/ordenes/nueva/` → Crear orden
- `/ordenes/buscar/` → Buscar órdenes por nombre del cliente

---

## 🧩 Modelos

### Product

```python
name: CharField
price: FloatField
description: TextField
```

### Client

```python
name: CharField
lastname: CharField
email: EmailField
```

### Order

```python
client: ForeignKey(Client)
products: ManyToManyField(Product)
created_at: DateTimeField (auto)
```

---

## ✍️ Notas

- Las búsquedas utilizan `Q()` de Django para permitir filtrar por múltiples campos.
- Los formularios están hechos con HTML simple + clases Bootstrap para estilo básico.
- El campo `created_at` se usa en órdenes para mostrar cuándo fue creada cada orden.

---

## 🚀 Mejoras posibles a futuro

- Agregar autenticación de usuarios
- Permitir edición y eliminación de productos/clientes/órdenes
- Soporte para paginación
- Panel de administración personalizado

---
