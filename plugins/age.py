PLUGIN_NAME = "age"
PLUGIN_DESCRIPTION = "Calcula la edad exacta de una persona a partir de su fecha de nacimiento."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "age",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "birth_date": {"type": "string", "description": "Fecha de nacimiento en formato YYYY-MM-DD"}
            },
            "required": ["birth_date"]
        }
    }
}

def run(birth_date: str) -> str:
    from datetime import datetime
    try:
        birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_datetime.year - ((today.month, today.day) < (birth_datetime.month, birth_datetime.day))
        return f"La edad exacta es: {age} años."
    except ValueError:
        return "Error: Formato de fecha inválido. Use YYYY-MM-DD."
    except Exception as e:
        return f"Error inesperado al calcular la edad: {e}"
