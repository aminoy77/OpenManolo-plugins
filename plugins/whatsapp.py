PLUGIN_NAME = "whatsapp"
PLUGIN_DESCRIPTION = "Envía mensajes vía WhatsApp Web (simulado, requiere configuración manual o Selenium)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "whatsapp",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "phone_number": {"type": "string", "description": "Número de teléfono del destinatario (con código de país, ej. +34600123456)"},
                "message": {"type": "string", "description": "Mensaje a enviar"}
            },
            "required": ["phone_number", "message"]
        }
    }
}

def run(phone_number: str, message: str) -> str:
    # Enviar mensajes por WhatsApp de forma programática es complejo y a menudo requiere
    # el uso de Selenium para automatizar WhatsApp Web, o la API oficial de WhatsApp Business,
    # que tiene requisitos específicos y costos.
    # Para este plugin, simularemos el envío.
    return f"Mensaje simulado enviado a {phone_number} vía WhatsApp: \"{message}\". (Requiere configuración manual o Selenium para uso real)"
