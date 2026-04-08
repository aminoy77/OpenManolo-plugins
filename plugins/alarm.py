PLUGIN_NAME = "alarm"
PLUGIN_DESCRIPTION = "Programa alarmas con un mensaje y hora específicos."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "alarm",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "time": {"type": "string", "description": "Hora de la alarma en formato HH:MM (ej. 07:30)"},
                "message": {"type": "string", "description": "Mensaje de la alarma"}
            },
            "required": ["time", "message"]
        }
    }
}

# Simulación de almacenamiento de alarmas
alarms = []

def run(time: str, message: str) -> str:
    import datetime
    try:
        # Validar formato de hora
        datetime.datetime.strptime(time, "%H:%M").time()
        alarms.append({"time": time, "message": message})
        # En un sistema real, esto programaría una alarma en el sistema operativo o un hilo.
        return f"Alarma programada para las {time} con el mensaje: \"{message}\". (Simulado)"
    except ValueError:
        return "Error: Formato de hora inválido. Use HH:MM (ej. 07:30)."
    except Exception as e:
        return f"Error inesperado al programar la alarma: {e}"
