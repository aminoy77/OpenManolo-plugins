PLUGIN_NAME = "bus"
PLUGIN_DESCRIPTION = "Obtiene horarios de autobuses y metros en ciudades españolas (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "bus",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Ciudad (ej. Madrid, Barcelona)"},
                "line": {"type": "string", "description": "Número o nombre de la línea (ej. 27, L1)"},
                "stop": {"type": "string", "description": "Parada o estación (opcional)"}
            },
            "required": ["city", "line"]
        }
    }
}

def run(city: str, line: str, stop: str = None) -> str:
    # La obtención de horarios de transporte público en tiempo real requiere integración con APIs específicas
    # de cada ciudad o empresa de transporte, las cuales suelen requerir autenticación.
    # Para este plugin, simularemos la funcionalidad.
    city_lower = city.lower()
    line_upper = line.upper()

    if city_lower == "madrid":
        if line_upper == "27":
            return f"Horarios de autobús línea 27 en Madrid (simulado): Próximo bus en 5 min. (Parada: {stop if stop else 'general'})."
        elif line_upper == "L1":
            return f"Horarios de metro línea L1 en Madrid (simulado): Próximo tren en 3 min. (Estación: {stop if stop else 'general'})."
        else:
            return f"No se encontraron horarios para la línea {line} en Madrid (simulado)."
    elif city_lower == "barcelona":
        if line_upper == "H12":
            return f"Horarios de autobús línea H12 en Barcelona (simulado): Próximo bus en 7 min. (Parada: {stop if stop else 'general'})."
        elif line_upper == "L3":
            return f"Horarios de metro línea L3 en Barcelona (simulado): Próximo tren en 4 min. (Estación: {stop if stop else 'general'})."
        else:
            return f"No se encontraron horarios para la línea {line} en Barcelona (simulado)."
    else:
        return f"No se encontraron horarios para la ciudad {city} (simulado)."
