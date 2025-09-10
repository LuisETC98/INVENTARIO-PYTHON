from db import get_connection

def agregar_producto(codigo, nombre, precio, cantidad):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO products (codigo, nombre, precio, cantidad) VALUES (?, ?, ?, ?)",
            (codigo, nombre, precio, cantidad)
        )
        conn.commit()

def listar_productos():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM products ORDER BY codigo").fetchall()

def actualizar_producto(codigo, nombre=None, precio=None, cantidad=None):
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM products WHERE codigo = ?", (codigo,))
        row = cur.fetchone()
        if not row:
            return False  # No existe

        nuevo_nombre = nombre if nombre else row["nombre"]
        nuevo_precio = precio if precio else row["precio"]
        nueva_cantidad = cantidad if cantidad else row["cantidad"]

        conn.execute(
            "UPDATE products SET nombre = ?, precio = ?, cantidad = ? WHERE codigo = ?",
            (nuevo_nombre, nuevo_precio, nueva_cantidad, codigo)
        )
        conn.commit()
        return True

def eliminar_producto(codigo):
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM products WHERE codigo = ?", (codigo,))
        conn.commit()
        return cur.rowcount > 0  # True si eliminó algo