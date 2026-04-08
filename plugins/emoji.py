PLUGIN_NAME = "emoji"
PLUGIN_DESCRIPTION = "Busca emojis por palabra clave y genera emojis aleatorios."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "emoji",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (search, random)",
                    "enum": ["search", "random"]
                },
                "query": {
                    "type": "string",
                    "description": "Palabra clave para buscar emojis (requerido para \'search\')"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, query: str = None) -> str:
    import random
    # Una lista simplificada de emojis para demostración.
    # En un entorno real, se usaría una librería como `emoji` o una base de datos de emojis.
    emoji_data = {
        "feliz": ["😊", "😄", "😁"],
        "triste": ["😔", "😢", "😭"],
        "amor": ["❤️", "😍", "🥰"],
        "mano": ["👋", "👍", "👏"],
        "comida": ["🍕", "🍔", "🍟"],
        "aleatorio": ["✨", "🚀", "💡", "🎉", "🌟", "🌈"]
    }

    if action == "search":
        if not query:
            return "Error: Se requiere una palabra clave para buscar emojis."
        found_emojis = []
        for keyword, emojis in emoji_data.items():
            if query.lower() in keyword:
                found_emojis.extend(emojis)
        if found_emojis:
            return f"Emojis para \'{query}\': {" ".join(found_emojis)}"
        else:
            return f"No se encontraron emojis para \'{query}\'."
    elif action == "random":
        all_emojis = [e for sublist in emoji_data.values() for e in sublist]
        return random.choice(all_emojis)
    else:
        return "Acción de emoji no reconocida."
