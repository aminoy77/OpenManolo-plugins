PLUGIN_NAME = "weather"
PLUGIN_DESCRIPTION = "Obtiene el clima actual y el pronóstico para cualquier ciudad."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "weather",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Nombre de la ciudad"},
                "forecast_days": {"type": "integer", "description": "Número de días para el pronóstico (1-3)", "default": 1}
            },
            "required": ["city"]
        }
    }
}

def run(city: str, forecast_days: int = 1) -> str:
    import httpx
    try:
        # Usaremos la API de Open-Meteo para un ejemplo sencillo y gratuito.
        # En un entorno real, se podría usar una API más robusta como OpenWeatherMap con clave API.
        url = f"https://api.open-meteo.com/v1/forecast?latitude=0&longitude=0&current_weather=true&forecast_days={forecast_days}&timezone=auto"
        # Para obtener latitud y longitud, se necesitaría una API de geocodificación. Simularemos para una ciudad.
        # Por simplicidad, usaremos valores fijos para algunas ciudades o un valor por defecto.
        if city.lower() == "madrid":
            lat, lon = 40.4168, -3.7038
        elif city.lower() == "barcelona":
            lat, lon = 41.3851, 2.1734
        else:
            # Valor por defecto o error si no se encuentra la ciudad
            return f"Error: No se pudo obtener la ubicación para {city}. Intenta con Madrid o Barcelona (simulado)."

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&forecast_days={forecast_days}&timezone=auto"
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data.get("current_weather", {})
        temperature = current.get("temperature")
        windspeed = current.get("windspeed")
        weathercode = current.get("weathercode")

        weather_description = {
            0: "Cielo despejado", 1: "Mayormente despejado", 2: "Parcialmente nublado", 3: "Nublado",
            45: "Niebla", 48: "Niebla helada",
            51: "Llovizna ligera", 53: "Llovizna moderada", 55: "Llovizna densa",
            56: "Llovizna helada ligera", 57: "Llovizna helada densa",
            61: "Lluvia ligera", 63: "Lluvia moderada", 65: "Lluvia fuerte",
            66: "Lluvia helada ligera", 67: "Lluvia helada fuerte",
            71: "Nevada ligera", 73: "Nevada moderada", 75: "Nevada fuerte",
            77: "Granizo",
            80: "Chubascos ligeros", 81: "Chubascos moderados", 82: "Chubascos violentos",
            85: "Nieve ligera", 86: "Nieve fuerte",
            95: "Tormenta", 96: "Tormenta con granizo ligero", 99: "Tormenta con granizo fuerte"
        }.get(weathercode, "Desconocido")

        output = f"Clima actual en {city.capitalize()}:\n"
        output += f"Temperatura: {temperature}°C\n"
        output += f"Velocidad del viento: {windspeed} km/h\n"
        output += f"Condición: {weather_description}"

        if forecast_days > 1:
            # La API de Open-Meteo requiere más parámetros para el pronóstico detallado.
            # Por simplicidad, solo indicaremos que el pronóstico está disponible.
            output += f"\nPronóstico para los próximos {forecast_days} días disponible (detalles no implementados en esta simulación)."

        return output
    except httpx.RequestError as e:
        return f"Error de conexión al obtener el clima: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al obtener el clima: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al obtener el clima: {e}"
