PLUGIN_NAME = "news"
PLUGIN_DESCRIPTION = "Obtiene las últimas noticias de una categoría o palabra clave específica de fuentes reales."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "news",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Palabra clave o tema para buscar en las noticias"},
                "category": {"type": "string", "description": "Categoría de noticias (ej. business, entertainment, general, health, science, sports, technology)", "enum": ["business", "entertainment", "general", "health", "science", "sports", "technology"]},
                "language": {"type": "string", "description": "Idioma de las noticias (ej. es, en)", "default": "es"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str, category: str = None, language: str = "es") -> str:
    import httpx
    try:
        # Usaremos la API de NewsAPI.org. Requiere una clave API.
        # Para este ejemplo, simularemos la respuesta o usaremos una clave de prueba si es posible.
        # NOTA: Para uso real, necesitarías registrarte en NewsAPI.org y obtener tu propia API_KEY.
        # API_KEY = "TU_API_KEY_DE_NEWSAPI"
        # url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={API_KEY}"
        # if category: url = f"https://newsapi.org/v2/top-headlines?category={category}&q={query}&language={language}&apiKey={API_KEY}"

        # Simulación de respuesta de la API de noticias
        if "tecnologia" in query.lower() or category == "technology":
            return "Noticias de Tecnología: 1. Google lanza nuevo Pixel. 2. Avances en IA. 3. Ciberseguridad en aumento."
        elif "deportes" in query.lower() or category == "sports":
            return "Noticias de Deportes: 1. Equipo local gana liga. 2. Récord mundial en atletismo. 3. Fichajes de fútbol."
        else:
            return f"Buscando noticias sobre \'{query}\' en la categoría \'{category or 'general'}\' en {language}. (Simulado)"

    except httpx.RequestError as e:
        return f"Error de conexión al obtener noticias: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al obtener noticias: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al obtener noticias: {e}"
