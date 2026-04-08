PLUGIN_NAME = "movie"
PLUGIN_DESCRIPTION = "Busca información de películas y series (sinopsis, reparto, puntuación)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "movie",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Título de la película o serie a buscar"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str) -> str:
    import httpx
    try:
        # Usaremos la API de OMDb (requiere una clave API gratuita).
        # Para este ejemplo, simularemos una respuesta.
        if "interstellar" in query.lower():
            return "Película: Interstellar (2014). Sinopsis: Un equipo de exploradores viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad. Director: Christopher Nolan. Puntuación: 8.6/10 (IMDb)."
        elif "inception" in query.lower():
            return "Película: Inception (2010). Sinopsis: Un ladrón que roba secretos corporativos a través del uso de tecnología de compartir sueños recibe la tarea inversa de implantar una idea en la mente de un C.E.O. Director: Christopher Nolan. Puntuación: 8.8/10 (IMDb)."
        else:
            return f"Buscando información para \'{query}\'. No se encontraron resultados específicos. (Simulado)"
    except Exception as e:
        return f"Error al buscar información de películas/series: {e}"
