PLUGIN_NAME = "reminder"
PLUGIN_DESCRIPTION = "Establece recordatorios con fecha y hora específicas."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "reminder",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "datetime_str": {
                    "type": "string",
                    "description": "Fecha y hora del recordatorio (ej. \"2026-04-08 10:30\")"
                },
                "message": {
                    "type": "string",
                    "description": "Mensaje del recordatorio"
                }
            },
            "required": ["datetime_str", "message"]
        }
    }
}

# Simulación de almacenamiento de recordatorios
reminders = []

def run(datetime_str: str, message: str) -> str:
    import datetime
    try:
        dt_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        reminders.append({"datetime": dt_obj, "message": message})
        # En un sistema real, esto programaría una notificación o evento.
        return f"Recordatorio establecido para {datetime_str}: {message}"
    except ValueError:
        return "Error: Formato de fecha y hora inválido. Use YYYY-MM-DD HH:MM."
    except Exception as e:
        return f"Error inesperado al establecer el recordatorio: {e}"
