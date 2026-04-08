PLUGIN_NAME = "voice"
PLUGIN_DESCRIPTION = "Convierte texto a voz y reproduce el audio (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "voice",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "El texto a convertir en voz"},
                "language": {"type": "string", "description": "Idioma para la síntesis de voz (ej. es, en)", "default": "es"}
            },
            "required": ["text"]
        }
    }
}

def run(text: str, language: str = "es") -> str:
    # En un entorno real, esto usaría librerías como `gTTS` (Google Text-to-Speech)
    # o `pyttsx3` para síntesis de voz, y `playsound` o `pydub` para reproducción.
    # Para este plugin, simularemos la acción.
    return f"Texto convertido a voz en {language} y reproducido: \"{text}\". (Simulado)"
