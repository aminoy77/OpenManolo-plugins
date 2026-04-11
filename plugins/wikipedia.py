PLUGIN_NAME = "wikipedia"
PLUGIN_DESCRIPTION = "Busca y resume información de Wikipedia en español."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "wikipedia",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "El término de búsqueda en Wikipedia"},
                "sentences": {"type": "integer", "description": "Número de oraciones para el resumen", "default": 3}
            },
            "required": ["query"]
        }
    }
}

def run(query: str, sentences: int = 3) -> str:
    try:
        import wikipedia
        wikipedia.set_lang("es")

        try:
            # Buscar la página y obtener el resumen
            summary = wikipedia.summary(query, sentences=sentences)
            return f"Resumen de Wikipedia para \'{query}\':\n{summary}"
        except wikipedia.exceptions.PageError:
            return f"Error: No se encontró ninguna página de Wikipedia para \'{query}\'."
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Error: La búsqueda \'{query}\' es ambigua. Intenta ser más específico. Posibles opciones: {e.options[:5]}"
    except ImportError:
        return "ERROR: La librería \'wikipedia\' no está instalada. Ejecuta: pip3 install wikipedia --break-system-packages"
    except Exception as e:
        return f"Error al buscar en Wikipedia: {e}"
