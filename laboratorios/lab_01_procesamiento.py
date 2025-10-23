# Archivo: lab_01_procesamiento.py
"""
Laboratorio 1: Procesamiento de Datos
Objetivo: Practicar el uso de bucles para procesar datos

La función debe:
1. Calcular el total de ventas
2. Encontrar la venta más alta
3. Contar ventas superiores a un umbral
"""

def analizar_ventas(ventas, umbral):
    """
    Analiza una lista de ventas y genera estadísticas
    Args:
        ventas (list): Lista de montos de ventas
        umbral (float): Valor para comparar ventas
    Returns:
        dict: Diccionario con estadísticas de ventas
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa la función
    """
    # TODO: Implementar el análisis siguiendo estos pasos:
    # 1. Inicializar variables para:
    #    - total_ventas (suma de todas las ventas)
    #    - venta_maxima (la venta más alta)
    #    - ventas_altas (contador de ventas > umbral)
    
    
    # TODO: Escribe tu código de inicialización aquí
    
    
    # 2. Recorrer la lista de ventas y:
    #    - Sumar cada venta al total
    #    - Actualizar venta_maxima si corresponde
    #    - Incrementar ventas_altas si la venta supera el umbral
    
    
    # TODO: Escribe tu código de procesamiento aquí
    
    
    # 3. Retornar un diccionario con los resultados:
    #return {
    #        "total": total_ventas,
    #        "maxima": venta_maxima,
    #        "num_ventas_altas": ventas_altas
    #    }
    
    # Por ahora, lanzamos NotImplementedError para indicar que falta implementar
    raise NotImplementedError("¡Función no implementada! Debes escribir el código de análisis.")

def main():
    # Casos de prueba
    ventas_dia = [100, 200, 50, 300, 150, 80]
    umbral_alto = 150
    
    print("=== Análisis de Ventas ===")
    print(f"Ventas del día: {ventas_dia}")
    print(f"Umbral para ventas altas: ${umbral_alto}")
    
    try:
        resultados = analizar_ventas(ventas_dia, umbral_alto)
        print("\nResultados:")
        print(f"Total de ventas: ${resultados['total']}")
        print(f"Venta más alta: ${resultados['maxima']}")
        print(f"Número de ventas altas: {resultados['num_ventas_altas']}")
    except NotImplementedError as e:
        print(f"\nEstado: {str(e)}")

if __name__ == "__main__":
    main()