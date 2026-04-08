PLUGIN_NAME = "flight"
PLUGIN_DESCRIPTION = "Obtiene información de vuelos (estado, precios aproximados, horarios)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "flight",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "flight_number": {"type": "string", "description": "Número de vuelo (ej. IB3100)"},
                "origin": {"type": "string", "description": "Código IATA del aeropuerto de origen (ej. MAD)"},
                "destination": {"type": "string", "description": "Código IATA del aeropuerto de destino (ej. BCN)"},
                "date": {"type": "string", "description": "Fecha del vuelo en formato YYYY-MM-DD"}
            },
            "required": []
        }
    }
}

def run(flight_number: str = None, origin: str = None, destination: str = None, date: str = None) -> str:
    # En un entorno real, esto se integraría con una API de vuelos (ej. FlightAware, Skyscanner).
    # Se necesitaría una clave API y manejar la búsqueda de vuelos.
    # Aquí se simula la funcionalidad.
    if flight_number:
        if flight_number.upper() == "IB3100":
            return f"Información de vuelo para IB3100 (simulado): Estado: A tiempo. Origen: Madrid (MAD). Destino: Barcelona (BCN). Salida: 10:00. Llegada: 11:15."
        else:
            return f"No se encontró información para el vuelo {flight_number} (simulado)."
    elif origin and destination and date:
        return f"Buscando vuelos de {origin} a {destination} para el {date} (simulado): Precios aproximados desde 50 EUR. Varias opciones disponibles."
    else:
        return "Por favor, proporciona un número de vuelo o el origen, destino y fecha para buscar."
