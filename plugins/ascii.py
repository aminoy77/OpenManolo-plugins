PLUGIN_NAME = "ascii"
PLUGIN_DESCRIPTION = "Convierte texto en arte ASCII."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "ascii",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "El texto a convertir en arte ASCII"}
            },
            "required": ["text"]
        }
    }
}

def run(text: str) -> str:
    try:
        from art import text2art
        ascii_art = text2art(text)
        return ascii_art
    except ImportError:
        return "Error: La librería \'art\' no está instalada. Por favor, instálala con \'pip install art\'."
    except Exception as e:
        return f"Error al generar arte ASCII: {e}"
