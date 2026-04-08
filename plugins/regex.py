PLUGIN_NAME = "regex"
PLUGIN_DESCRIPTION = "Testea y explica expresiones regulares, mostrando coincidencias en un texto."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "regex",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "La expresión regular a usar"},
                "text": {"type": "string", "description": "El texto donde buscar coincidencias"},
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (match, search, findall, explain)",
                    "enum": ["match", "search", "findall", "explain"],
                    "default": "findall"
                }
            },
            "required": ["pattern", "text"]
        }
    }
}

def run(pattern: str, text: str, action: str = "findall") -> str:
    import re

    try:
        if action == "match":
            match = re.match(pattern, text)
            return f"Match: {match.group(0)}" if match else "No hay coincidencia al inicio del texto."
        elif action == "search":
            search = re.search(pattern, text)
            return f"Search: {search.group(0)}" if search else "No se encontró coincidencia en el texto."
        elif action == "findall":
            findall = re.findall(pattern, text)
            return f"FindAll: {findall}" if findall else "No se encontraron coincidencias en el texto."
        elif action == "explain":
            # La explicación de regex es compleja y no hay una librería estándar simple para ello.
            # Se simulará una explicación básica.
            explanation = f"Explicación básica para 
{pattern}
: Este patrón busca secuencias de caracteres que coincidan con la definición proporcionada. Para una explicación detallada, consulta herramientas online de regex."
            return explanation
        else:
            return "Acción de regex no reconocida."
    except re.error as e:
        return f"Error en la expresión regular: {e}"
    except Exception as e:
        return f"Error inesperado en el plugin regex: {e}"
