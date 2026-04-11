PLUGIN_NAME = "translate"
PLUGIN_DESCRIPTION = "Traduce texto entre diferentes idiomas utilizando deep-translator."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "translate",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "El texto a traducir"},
                "target_lang": {"type": "string", "description": "El idioma de destino (ej. es, en, fr)"},
                "source_lang": {"type": "string", "description": "El idioma de origen (opcional, si se omite, se detecta automáticamente)", "default": "auto"}
            },
            "required": ["text", "target_lang"]
        }
    }
}

def run(text: str, target_lang: str, source_lang: str = "auto") -> str:
    try:
        from deep_translator import GoogleTranslator

        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(text)

        if translated_text:
            return f"Texto original: {text}\nIdioma de origen: {source_lang}\nIdioma de destino: {target_lang}\nTraducción: {translated_text}"
        else:
            return "Error: No se pudo realizar la traducción. Verifica los idiomas o el texto."
    except ImportError:
        return "ERROR: La librería \'deep-translator\' no está instalada. Ejecuta: pip3 install deep-translator --break-system-packages"
    except Exception as e:
        return f"Error al traducir texto: {e}"
