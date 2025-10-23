# Archivo: lab_02_filtrado.py
"""
Laboratorio 2: Filtrado de Datos
Objetivo: Practicar filtrado de datos usando bucles y condiciones

La función debe filtrar productos según múltiples criterios:
1. Precio dentro de un rango (min_precio, max_precio)
2. Stock disponible mayor a 0
3. Categoría específica
"""

def filtrar_productos(productos, min_precio, max_precio, categoria):
    """
    Filtra una lista de productos según criterios específicos
    Args:
        productos (list): Lista de diccionarios con información de productos
        min_precio (float): Precio mínimo a considerar
        max_precio (float): Precio máximo a considerar
        categoria (str): Categoría de productos a filtrar
    Returns:
        list: Lista de productos que cumplen los criterios
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa la función
    """
    # TODO: Implementar el filtrado siguiendo estos pasos:
    # 1. Crear una lista vacía para los productos filtrados
    
    # TODO: Escribe tu código de inicialización aquí
    
    
    # 2. Recorrer la lista de productos y por cada uno:
    #    - Verificar que el precio esté en el rango
    #    - Verificar que haya stock disponible
    #    - Verificar que sea de la categoría solicitada
    #    Si cumple todos los criterios, agregarlo a la lista filtrada
    
    # TODO: Escribe tu código de filtrado aquí
    
    
    # 3. Retornar la lista de productos filtrados
    
    # Por ahora, lanzamos NotImplementedError para indicar que falta implementar
    raise NotImplementedError("¡Función no implementada! Debes escribir el código de filtrado.")

def main():
    # Casos de prueba
    productos = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "stock": 10, "categoria": "Electrónica"},
        {"nombre": "Libro", "precio": 30, "stock": 0, "categoria": "Libros"},
        {"nombre": "Monitor", "precio": 300, "stock": 3, "categoria": "Electrónica"}
    ]
    
    print("=== Filtrado de Productos ===")
    print("\nCriterios de filtrado:")
    print("- Precio entre $20 y $500")
    print("- Con stock disponible")
    print("- Categoría: Electrónica")
    
    try:
        filtrados = filtrar_productos(productos, 20, 500, "Electrónica")
        print("\nProductos que cumplen los criterios:")
        for producto in filtrados:
            print(f"- {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
    except NotImplementedError as e:
        print(f"\nEstado: {str(e)}")

if __name__ == "__main__":
    main()