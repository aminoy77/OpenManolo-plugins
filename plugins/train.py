PLUGIN_NAME = "train"
PLUGIN_DESCRIPTION = "Obtiene horarios de trenes (Renfe, AVE, etc.) entre dos estaciones."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "train",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {"type": "string", "description": "Estación de origen"},
                "destination": {"type": "string", "description": "Estación de destino"},
                "date": {"type": "string", "description": "Fecha del viaje en formato YYYY-MM-DD"}
            },
            "required": ["origin", "destination", "date"]
        }
    }
}

def run(origin: str, destination: str, date: str) -> str:
    # La obtención de horarios de trenes en tiempo real requiere integración con APIs específicas
    # de operadores como Renfe, las cuales suelen requerir autenticación y son de pago.
    # Para este plugin, simularemos la funcionalidad.
    if origin.lower() == "madrid" and destination.lower() == "barcelona":
        return f"Horarios de trenes de Madrid a Barcelona para el {date} (simulado):\n  AVE: 09:00, 12:00, 15:00. Duración: 2h 30min. Precios desde 50 EUR."
    else:
        return f"No se encontraron horarios de trenes para {origin} a {destination} en la fecha {date} (simulado)."
