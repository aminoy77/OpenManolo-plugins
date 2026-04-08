PLUGIN_NAME = "definition"
PLUGIN_DESCRIPTION = "Busca la definición de una palabra en español."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "definition",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "word": {"type": "string", "description": "La palabra a buscar"}
            },
            "required": ["word"]
        }
    }
}

def run(word: str) -> str:
    import httpx
    try:
        # Usaremos una API de diccionario gratuita como ejemplo. Por ejemplo, Free Dictionary API.
        # En un entorno real, se podría usar la API de la RAE o similar.
        url = f"https://api.dictionaryapi.dev/api/v2/entries/es/{word}"
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            definitions = []
            for entry in data:
                for meaning in entry.get("meanings", []):
                    part_of_speech = meaning.get("partOfSpeech", "")
                    for definition_obj in meaning.get("definitions", []):
                        definitions.append(f"({part_of_speech}) {definition_obj.get("definition")}")
            if definitions:
                return f"Definiciones de ‘{word}’:\n" + "\n".join(definitions)
            else:
                return f"No se encontraron definiciones para ‘{word}’."
        else:
            return f"No se encontraron definiciones para ‘{word}’."
    except httpx.RequestError as e:
        return f"Error de conexión al buscar la definición: {e}"
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return f"No se encontró la palabra ‘{word}’ en el diccionario."
        return f"Error HTTP al buscar la definición: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al buscar la definición: {e}"
