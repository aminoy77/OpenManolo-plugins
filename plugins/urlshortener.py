PLUGIN_NAME = "urlshortener"
PLUGIN_DESCRIPTION = "Acorta una URL larga utilizando el servicio TinyURL."
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
    try:
        import httpx

        api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        
        short_url = response.text.strip()
        
        if short_url.startswith("http"):
            return f"URL acortada: {short_url}"
        else:
            return f"Error al acortar la URL: {short_url}"
    except httpx.RequestError as e:
        return f"Error de conexión al servicio TinyURL: {e}"
    except Exception as e:
        return f"Error al acortar la URL: {e}"
