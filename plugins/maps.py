PLUGIN_NAME = "maps"
PLUGIN_DESCRIPTION = "Obtiene direcciones y calcula distancias entre dos ubicaciones (ciudades o direcciones específicas)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "maps",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {"type": "string", "description": "Punto de origen (ej. \"Madrid\", \"Calle Mayor 1, Madrid\")"},
                "destination": {"type": "string", "description": "Punto de destino (ej. \"Barcelona\", \"Plaza Cataluña 1, Barcelona\")"},
                "mode": {
                    "type": "string",
                    "description": "Modo de transporte (driving, walking, bicycling, transit)",
                    "enum": ["driving", "walking", "bicycling", "transit"],
                    "default": "driving"
                }
            },
            "required": ["origin", "destination"]
        }
    }
}

def run(origin: str, destination: str, mode: str = "driving") -> str:
    import httpx
    # En un entorno real, esto se integraría con una API de mapas como Google Maps API o OpenStreetMap Nominatim/OSRM.
    # Se necesitaría una clave API y manejar la geocodificación y el cálculo de rutas.
    # Aquí se simula la funcionalidad.
    if "madrid" in origin.lower() and "barcelona" in destination.lower():
        if mode == "driving":
            return f"Ruta de {origin} a {destination} ({mode}): Distancia aproximada: 620 km, Tiempo estimado: 6 horas. (Simulado)"
        else:
            return f"Ruta de {origin} a {destination} ({mode}): Distancia y tiempo simulados para {mode}. (Simulado)"
    else:
        return f"No se pudo calcular la ruta para {origin} a {destination}. (Simulado: solo se admiten rutas Madrid-Barcelona por ahora)"
