PLUGIN_NAME = "urlshortener"
PLUGIN_DESCRIPTION = "Acorta una URL larga utilizando un servicio de acortamiento de enlaces."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "urlshortener",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "long_url": {"type": "string", "description": "La URL larga a acortar"}
            },
            "required": ["long_url"]
        }
    }
}

def run(long_url: str) -> str:
    import httpx
    try:
        # Usaremos la API de TinyURL como ejemplo, ya que es sencilla y no requiere autenticación para uso básico.
        api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()
        short_url = response.text.strip()
        if short_url.startswith("http"): # TinyURL devuelve la URL acortada o un mensaje de error
            return f"URL acortada: {short_url}"
        else:
            return f"Error al acortar la URL: {short_url}"
    except httpx.RequestError as e:
        return f"Error de conexión al acortar la URL: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al acortar la URL: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al acortar la URL: {e}"
