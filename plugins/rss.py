PLUGIN_NAME = "rss"
PLUGIN_DESCRIPTION = "Lee feeds RSS y noticias por temática de una URL específica."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "rss",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "feed_url": {"type": "string", "description": "URL del feed RSS (ej. https://www.meneame.net/rss)"},
                "limit": {"type": "integer", "description": "Número máximo de noticias a devolver", "default": 5}
            },
            "required": ["feed_url"]
        }
    }
}

def run(feed_url: str, limit: int = 5) -> str:
    import feedparser
    try:
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            return f"Error al parsear el feed RSS: {feed.bozo_exception}"

        if not feed.entries:
            return "No se encontraron noticias en el feed RSS."

        output = f"Noticias de {feed.feed.title}:\n"
        for i, entry in enumerate(feed.entries):
            if i >= limit:
                break
            output += f"- {entry.title}\n  Enlace: {entry.link}\n"
        return output
    except Exception as e:
        return f"Error inesperado al leer el feed RSS: {e}"
