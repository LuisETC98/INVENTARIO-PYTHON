import csv
from db import get_connection

def generar_reporte_csv(filename="reporte_inventario.csv"):
    with get_connection() as conn:
        cur = conn.execute("SELECT codigo, nombre, precio, cantidad FROM products ORDER BY codigo")
        rows = cur.fetchall()

        if not rows:
            return None  # No hay datos

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["codigo", "nombre", "precio", "cantidad"])
            for r in rows:
                writer.writerow([r["codigo"], r["nombre"], r["precio"], r["cantidad"]])

    return filename