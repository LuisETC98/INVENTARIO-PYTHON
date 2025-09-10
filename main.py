from db import init_db
from crud import agregar_producto, listar_productos, actualizar_producto, eliminar_producto
from utils import generar_reporte_csv

def menu():
    init_db()  # Asegura que la tabla exista
    while True:
        print("""
Bienvenido al programa de inventario. Elija una opción:
1- Agregar producto
2- Actualizar producto
3- Mostrar inventario
4- Eliminar producto
5- Generar reporte CSV
6- Salir
""")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                codigo = int(input("Código: "))
                nombre = input("Nombre: ")
                precio = int(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(codigo, nombre, precio, cantidad)
                print("Producto agregado.")
            except Exception as e:
                print("Error al agregar producto:", e)

        elif opcion == "2":
            codigo = int(input("Código del producto a actualizar: "))
            nombre = input("Nuevo nombre (enter para mantener): ").strip() or None
            precio = input("Nuevo precio (enter para mantener): ").strip()
            cantidad = input("Nueva cantidad (enter para mantener): ").strip()
            precio = int(precio) if precio else None
            cantidad = int(cantidad) if cantidad else None

            if actualizar_producto(codigo, nombre, precio, cantidad):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            productos = listar_productos()
            if not productos:
                print("Inventario vacío.")
            else:
                print("-" * 72)
                print(f"{'Código':8} | {'Nombre':35} | {'Precio':8} | {'Cantidad':8}")
                print("-" * 72)
                for p in productos:
                    print(f"{p['codigo']:8} | {p['nombre'][:35]:35} | {p['precio']:8} | {p['cantidad']:8}")
                print("-" * 72)

        elif opcion == "4":
            codigo = int(input("Código del producto a eliminar: "))
            if eliminar_producto(codigo):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            reporte = generar_reporte_csv()
            if reporte:
                print(f"Reporte generado: {reporte}")
            else:
                print("No hay datos para generar el reporte.")

        elif opcion == "6":
            print("Hasta pronto!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()