PLUGIN_NAME = "discord"
PLUGIN_DESCRIPTION = "Envía mensajes a canales de Discord utilizando un webhook."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "discord",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "webhook_url": {"type": "string", "description": "URL del webhook de Discord"},
                "message": {"type": "string", "description": "Mensaje a enviar al canal de Discord"}
            },
            "required": ["webhook_url", "message"]
        }
    }
}

def run(webhook_url: str, message: str) -> str:
    import httpx
    try:
        payload = {"content": message}
        response = httpx.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        return f"Mensaje enviado exitosamente a Discord a través del webhook."
    except httpx.RequestError as e:
        return f"Error de conexión al enviar mensaje a Discord: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al enviar mensaje a Discord: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al enviar mensaje a Discord: {e}"
