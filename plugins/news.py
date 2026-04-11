PLUGIN_NAME = "news"
PLUGIN_DESCRIPTION = "Obtiene las últimas noticias o busca noticias por palabras clave utilizando la GNews API."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "news",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Palabras clave para buscar noticias (opcional)", "default": ""},
                "lang": {"type": "string", "description": "Idioma de las noticias (ej. es, en, fr). Por defecto es \'es\'.", "default": "es"},
                "max_articles": {"type": "integer", "description": "Número máximo de artículos a devolver (máx. 5)", "default": 3}
            },
            "required": []
        }
    }
}

def run(query: str = "", lang: str = "es", max_articles: int = 3) -> str:
    try:
        import httpx

        # NOTA: La GNews API requiere una clave API. Puedes obtener una gratuita en https://gnews.io/
        # Por ahora, usaremos un placeholder. En un entorno real, deberías usar una variable de entorno.
        GNEWS_API_KEY = "YOUR_GNEWS_API_KEY" # Reemplaza con tu clave API real

        if GNEWS_API_KEY == "YOUR_GNEWS_API_KEY":
            return "ERROR: La GNews API Key no está configurada. Obtén una en https://gnews.io/ y actualiza el plugin."

        if max_articles > 5: max_articles = 5 # Limitar para evitar respuestas muy largas

        if query:
            api_url = f"https://gnews.io/api/v4/search?q={query}&lang={lang}&max={max_articles}&token={GNEWS_API_KEY}"
        else:
            api_url = f"https://gnews.io/api/v4/top-headlines?lang={lang}&max={max_articles}&token={GNEWS_API_KEY}"

        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if not data or not data.get("articles"):
            return f"No se encontraron noticias para \'{query}\' en {lang}."

        output = []
        for i, article in enumerate(data["articles"]):
            output.append(f"--- Noticia {i+1} ---")
            output.append(f"Título: {article.get("title", "N/A")}")
            output.append(f"Fuente: {article.get("source", {}).get("name", "N/A")}")
            output.append(f"Publicado: {article.get("publishedAt", "N/A")}")
            output.append(f"Descripción: {article.get("description", "N/A")}")
            output.append(f"URL: {article.get("url", "N/A")}")

        return "\n\n".join(output)
    except httpx.RequestError as e:
        return f"Error de conexión al API de GNews: {e}"
    except Exception as e:
        return f"Error al obtener noticias: {e}"
