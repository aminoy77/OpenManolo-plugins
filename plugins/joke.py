PLUGIN_NAME = "joke"
PLUGIN_DESCRIPTION = "Cuenta un chiste aleatorio en español de varias categorías."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "joke",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Categoría del chiste (ej. Programming, Dark, Pun, Spooky, Christmas). Por defecto es \'Any\'.", "default": "Any"}
            },
            "required": []
        }
    }
}

def run(category: str = "Any") -> str:
    try:
        import httpx

        api_url = f"https://v2.jokeapi.dev/joke/{category}?lang=es&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if data.get("error"):
            return f"Error: No se pudo obtener un chiste para la categoría ‘{category}’. {data.get("message", "")}"

        if data["type"] == "single":
            return data["joke"]
        elif data["type"] == "twopart":
            return f"{data["setup"]}\n{data["delivery"]}"
        else:
            return "Error: Formato de chiste desconocido."
    except httpx.RequestError as e:
        return f"Error de conexión al API de chistes: {e}"
    except Exception as e:
        return f"Error al obtener un chiste: {e}"
