PLUGIN_NAME = "translatefile"
PLUGIN_DESCRIPTION = "Traduce el contenido de un archivo de texto completo a un idioma de destino."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "translatefile",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Ruta al archivo de texto a traducir"},
                "target_language": {"type": "string", "description": "El idioma al que se desea traducir (código ISO 639-1, ej. en, es, fr)"},
                "output_file_path": {"type": "string", "description": "Ruta donde guardar el archivo traducido (opcional)"}
            },
            "required": ["file_path", "target_language"]
        }
    }
}

def run(file_path: str, target_language: str, output_file_path: str = None) -> str:
    try:
        from deep_translator import GoogleTranslator
        import os

        if not os.path.exists(file_path):
            return f"Error: El archivo {file_path} no fue encontrado."

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        translated_content = GoogleTranslator(target=target_language).translate(content)

        if output_file_path:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            return f"Archivo traducido guardado en {output_file_path}"
        else:
            return f"Contenido traducido:\n{translated_content}"

    except ImportError:
        return "Error: La librería 'deep_translator' no está instalada. Por favor, instálala con 'pip install deep-translator'."
    except Exception as e:
        return f"Error al traducir el archivo: {e}"
