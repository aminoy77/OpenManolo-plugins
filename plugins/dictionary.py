PLUGIN_NAME = "dictionary"
PLUGIN_DESCRIPTION = "Diccionario avanzado para buscar definiciones, sinónimos, antónimos y ejemplos de uso."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "dictionary",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "word": {"type": "string", "description": "La palabra a buscar"},
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (define, synonyms, antonyms, examples)",
                    "enum": ["define", "synonyms", "antonyms", "examples"],
                    "default": "define"
                }
            },
            "required": ["word"]
        }
    }
}

def run(word: str, action: str = "define") -> str:
    import httpx
    try:
        # Usaremos la API de Free Dictionary como ejemplo.
        url = f"https://api.dictionaryapi.dev/api/v2/entries/es/{word}"
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list) or not data:
            return f"No se encontró información para la palabra ‘{word}’."

        output = []
        for entry in data:
            for meaning in entry.get("meanings", []):
                if action == "define":
                    for definition_obj in meaning.get("definitions", []):
                        output.append(f"- {definition_obj.get("definition")}")
                elif action == "synonyms":
                    synonyms = meaning.get("synonyms", [])
                    if synonyms: output.append(f"Sinónimos: {', '.join(synonyms)}")
                elif action == "antonyms":
                    antonyms = meaning.get("antonyms", [])
                    if antonyms: output.append(f"Antónimos: {', '.join(antonyms)}")
                elif action == "examples":
                    for definition_obj in meaning.get("definitions", []):
                        example = definition_obj.get("example")
                        if example: output.append(f"Ejemplo: \"{example}\"")

        if output:
            return f"Resultados para ‘{word}’ ({action}):\n" + "\n".join(output)
        else:
            return f"No se encontraron {action} para ‘{word}’."

    except httpx.RequestError as e:
        return f"Error de conexión al buscar en el diccionario: {e}"
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return f"No se encontró la palabra ‘{word}’ en el diccionario."
        return f"Error HTTP al buscar en el diccionario: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al buscar en el diccionario: {e}"
