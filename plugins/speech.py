PLUGIN_NAME = "speech"
PLUGIN_DESCRIPTION = "Realiza reconocimiento de voz a texto (simulado, requiere configuración de micrófono)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "speech",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "duration": {"type": "integer", "description": "Duración de la grabación en segundos", "default": 5},
                "language": {"type": "string", "description": "Idioma para el reconocimiento de voz (ej. es-ES, en-US)", "default": "es-ES"}
            },
            "required": []
        }
    }
}

def run(duration: int = 5, language: str = "es-ES") -> str:
    # En un entorno real, esto usaría librerías como `SpeechRecognition` con un motor como Google Speech Recognition,
    # o Vosk, o la API de Google Cloud Speech-to-Text. Requiere acceso al micrófono.
    # Para este plugin, simularemos la acción.
    return f"Grabando audio por {duration} segundos para reconocimiento de voz en {language}. (Simulado)\nTexto reconocido: \"Esto es una prueba de reconocimiento de voz.\""
