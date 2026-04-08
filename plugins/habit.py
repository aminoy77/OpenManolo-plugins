PLUGIN_NAME = "habit"
PLUGIN_DESCRIPTION = "Registra y gestiona hábitos diarios o semanales."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "habit",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (add, track, list, remove)",
                    "enum": ["add", "track", "list", "remove"]
                },
                "name": {
                    "type": "string",
                    "description": "Nombre del hábito (requerido para add, track, remove)"
                },
                "date": {
                    "type": "string",
                    "description": "Fecha para registrar el hábito (YYYY-MM-DD, por defecto hoy)"
                }
            },
            "required": ["action"]
        }
    }
}

# Simulación de almacenamiento de hábitos
habits = {}

def run(action: str, name: str = None, date: str = None) -> str:
    import datetime

    today = datetime.date.today().isoformat()
    track_date = date if date else today

    if action == "add":
        if not name:
            return "Error: El nombre del hábito es requerido para añadir."
        if name in habits:
            return f"Error: El hábito ‘{name}’ ya existe."
        habits[name] = []
        return f"Hábito ‘{name}’ añadido."
    elif action == "track":
        if not name:
            return "Error: El nombre del hábito es requerido para registrar."
        if name not in habits:
            return f"Error: El hábito ‘{name}’ no existe. Añádelo primero."
        if track_date in habits[name]:
            return f"El hábito ‘{name}’ ya fue registrado para el {track_date}."
        habits[name].append(track_date)
        return f"Hábito ‘{name}’ registrado para el {track_date}."
    elif action == "list":
        if not habits:
            return "No hay hábitos registrados."
        output = "Lista de Hábitos:\n"
        for habit_name, dates in habits.items():
            output += f"- {habit_name}: {len(dates)} veces registrado. Último: {max(dates) if dates else 'N/A'}\n"
        return output
    elif action == "remove":
        if not name:
            return "Error: El nombre del hábito es requerido para eliminar."
        if name in habits:
            del habits[name]
            return f"Hábito ‘{name}’ eliminado."
        else:
            return f"Error: El hábito ‘{name}’ no existe."
    else:
        return "Acción de hábito no reconocida."
