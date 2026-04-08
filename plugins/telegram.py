PLUGIN_NAME = "telegram"
PLUGIN_DESCRIPTION = "Envía mensajes o notificaciones a un chat de Telegram utilizando la API de Bot."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "telegram",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "bot_token": {"type": "string", "description": "Token de tu bot de Telegram"},
                "chat_id": {"type": "string", "description": "ID del chat o usuario al que enviar el mensaje"},
                "message": {"type": "string", "description": "Mensaje a enviar"}
            },
            "required": ["bot_token", "chat_id", "message"]
        }
    }
}

def run(bot_token: str, chat_id: str, message: str) -> str:
    import httpx
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = httpx.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return f"Mensaje enviado exitosamente a Telegram (chat ID: {chat_id})."
    except httpx.RequestError as e:
        return f"Error de conexión al enviar mensaje a Telegram: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al enviar mensaje a Telegram: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al enviar mensaje a Telegram: {e}"
