# Archivo: demo_01_bucles.py
"""
Demo 1: Bucles básicos
Objetivo: Mostrar el uso de bucles for y while para procesar datos
"""

def demo_bucles():
    print("=== Demo: Bucles Básicos ===")
    
    # Ejemplo 1: Bucle for con lista
    print("\nProcesando ventas diarias:")
    ventas_diarias = [120, 150, 80, 200, 95]
    total = 0
    
    for venta in ventas_diarias:
        total += venta
        print(f"Venta: ${venta} | Acumulado: ${total}")
    
    # Ejemplo 2: Bucle while con contador
    print("\nConteo regresivo de inventario:")
    stock = 5
    
    while stock > 0:
        print(f"Quedan {stock} unidades en stock")
        stock -= 1
    print("¡Inventario agotado!")

if __name__ == "__main__":
    demo_bucles()