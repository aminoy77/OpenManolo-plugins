PLUGIN_NAME = "twitter"
PLUGIN_DESCRIPTION = "Busca tweets recientes por palabra clave o muestra trending topics (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "twitter",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (search_tweets, trending_topics)",
                    "enum": ["search_tweets", "trending_topics"]
                },
                "query": {
                    "type": "string",
                    "description": "Palabra clave para buscar tweets (requerido para search_tweets)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, query: str = None) -> str:
    # La API de Twitter (ahora X) tiene restricciones y requiere autenticación.
    # Por lo tanto, esta funcionalidad será simulada.
    if action == "search_tweets":
        if not query:
            return "Error: Se requiere una palabra clave para buscar tweets."
        return f"Buscando tweets recientes para \'{query}\'. Resultados simulados: Tweet 1 sobre {query}, Tweet 2 sobre {query}."
    elif action == "trending_topics":
        return "Trending Topics simulados: #IA, #Python, #DesarrolloWeb, #NoticiasDelDia."
    else:
        return "Acción de Twitter no válida. Use \'search_tweets\' o \'trending_topics\'."
