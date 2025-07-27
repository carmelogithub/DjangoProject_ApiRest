# core/services.py
def procesar_datos(nombre, email, accion):
    # Aquí lógica segura: crear PDF, generar estadísticas, etc.
    if accion == 'analizar':
        return f"Análisis completo para {nombre} ({email})"
    elif accion == 'generar':
        return f"Informe generado para {nombre} ({email})"
    else:
        return "Acción desconocida"
