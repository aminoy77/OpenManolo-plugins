PLUGIN_NAME = "whois"
PLUGIN_DESCRIPTION = "Obtiene información WHOIS de un dominio, incluyendo datos de registro y contacto."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "whois",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "El nombre de dominio (ej. google.com)"}
            },
            "required": ["domain"]
        }
    }
}

def run(domain: str) -> str:
    try:
        import whois
        w = whois.whois(domain)
        return str(w)
    except ImportError:
        return "Error: La librería \'python-whois\' no está instalada. Por favor, instálala con \'pip install python-whois\'."
    except Exception as e:
        return f"Error al obtener información WHOIS: {e}"
