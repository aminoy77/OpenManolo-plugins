PLUGIN_NAME = "worldclock"
PLUGIN_DESCRIPTION = "Obtiene la hora actual en diferentes ciudades o zonas horarias del mundo."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "worldclock",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "city_or_timezone": {"type": "string", "description": "Nombre de la ciudad o zona horaria (ej. 'Europe/Madrid', 'America/New_York', 'Tokyo')"}
            },
            "required": ["city_or_timezone"]
        }
    }
}

def run(city_or_timezone: str) -> str:
    import datetime
    import pytz

    try:
        # Intentar interpretar como zona horaria directamente
        tz = pytz.timezone(city_or_timezone)
    except pytz.UnknownTimeZoneError:
        # Si no es una zona horaria, intentar mapear ciudades comunes a zonas horarias
        city_timezone_map = {
            "madrid": "Europe/Madrid",
            "barcelona": "Europe/Madrid",
            "london": "Europe/London",
            "new york": "America/New_York",
            "tokyo": "Asia/Tokyo",
            "sydney": "Australia/Sydney",
            "dubai": "Asia/Dubai",
            "paris": "Europe/Paris",
            "berlin": "Europe/Berlin",
            "los angeles": "America/Los_Angeles",
            "shanghai": "Asia/Shanghai",
            "moscow": "Europe/Moscow"
        }
        normalized_city = city_or_timezone.lower()
        if normalized_city in city_timezone_map:
            tz = pytz.timezone(city_timezone_map[normalized_city])
        else:
            return f"Error: Zona horaria o ciudad '{city_or_timezone}' no reconocida. Intenta con un formato como 'Europe/Madrid' o ciudades comunes como 'Madrid', 'Tokyo'."

    now_in_tz = datetime.datetime.now(tz)
    return f"La hora actual en {city_or_timezone} es: {now_in_tz.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
