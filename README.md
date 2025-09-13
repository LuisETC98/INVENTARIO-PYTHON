## Inventario con Python y SQLite

Programa simple de inventario en **Python**.  
Permite **agregar, actualizar, mostrar, eliminar** productos y **generar un reporte CSV**.  
Los datos se guardan en una base de datos local `inventario.db` (SQLite).

---

## Requisitos
- Python (utilicé la versión 3.13.2).
- SQLite viene incluido con Python

---

## Estructura del proyecto
inventario/
├── main.py # Menú principal (interfaz por consola)
├── db.py # Conexión e inicialización de la base de datos
├── crud.py # Funciones CRUD (agregar, listar, actualizar, eliminar)
├── utils.py # Funciones auxiliares (ej: generar reportes CSV)
├── inventario.db # Base de datos SQLite (se crea al ejecutar)
├── .gitignore
└── README.md
