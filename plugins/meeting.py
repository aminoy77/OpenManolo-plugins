PLUGIN_NAME = "meeting"
PLUGIN_DESCRIPTION = "Crea enlaces de reuniones para plataformas como Zoom, Google Meet o Microsoft Teams (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "meeting",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "platform": {
                    "type": "string",
                    "description": "Plataforma de la reunión (zoom, meet, teams)",
                    "enum": ["zoom", "meet", "teams"]
                },
                "topic": {"type": "string", "description": "Tema de la reunión"},
                "duration_minutes": {"type": "integer", "description": "Duración de la reunión en minutos", "default": 60}
            },
            "required": ["platform", "topic"]
        }
    }
}

def run(platform: str, topic: str, duration_minutes: int = 60) -> str:
    # La creación de enlaces de reuniones reales requiere integración con las APIs de cada plataforma
    # (Zoom API, Google Calendar API para Meet, Microsoft Graph API para Teams), lo cual implica
    # autenticación OAuth y configuración compleja. Por lo tanto, esta funcionalidad será simulada.
    if platform == "zoom":
        return f"Enlace de Zoom simulado creado para \"{topic}\" ({duration_minutes} min): https://zoom.us/j/simulated_id"
    elif platform == "meet":
        return f"Enlace de Google Meet simulado creado para \"{topic}\" ({duration_minutes} min): https://meet.google.com/simulated-code"
    elif platform == "teams":
        return f"Enlace de Microsoft Teams simulado creado para \"{topic}\" ({duration_minutes} min): https://teams.microsoft.com/l/meetup-join/simulated_id"
    else:
        return "Plataforma de reunión no reconocida. Use \"zoom\", \"meet\" o \"teams\"."
