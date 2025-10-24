# Archivo: demo_02_iteracion.py
"""
Demo 2: Técnicas de iteración
Objetivo: Mostrar técnicas avanzadas de iteración y control de bucles
"""

def demo_iteracion():
    print("=== Demo: Técnicas de Iteración ===")
    
    # Ejemplo 1: Enumerate para índices
    productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
    print("\nListado de productos:")
    
    for indice, producto in enumerate(productos, 1):
        print(f"{indice}. {producto}")
    
    # Ejemplo 2: Break y Continue
    print("\nBuscando productos en oferta:")
    precios = [100, 25, 80, 15, 200, 30, 50]
    limite_oferta = 50

    for precio in precios:
        if precio > limite_oferta:
            continue
        print(f"¡Oferta encontrada! Precio: ${precio}")

        if len([p for p in precios if p <= limite_oferta]) >= 3:
            print("¡Suficientes ofertas encontradas!")
            break

    
if __name__ == "__main__":
    demo_iteracion()