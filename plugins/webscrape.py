PLUGIN_NAME = "webscrape"
PLUGIN_DESCRIPTION = "Extrae información específica de cualquier página web utilizando selectores CSS o XPath."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "webscrape",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "La URL de la página web a scrapear"},
                "selector": {"type": "string", "description": "Selector CSS o XPath para el elemento a extraer"},
                "attribute": {"type": "string", "description": "Atributo a extraer del elemento (ej. 'href', 'src', 'text'). Por defecto, extrae el texto."}
            },
            "required": ["url", "selector"]
        }
    }
}

def run(url: str, selector: str, attribute: str = "text") -> str:
    import httpx
    from selectolax.parser import HTMLParser

    try:
        response = httpx.get(url, follow_redirects=True, timeout=10)
        response.raise_for_status()
        tree = HTMLParser(response.text)

        elements = tree.css(selector)
        if not elements:
            return f"No se encontraron elementos con el selector '{selector}' en la URL {url}."

        results = []
        for node in elements:
            if attribute == "text":
                results.append(node.text(strip=True))
            else:
                attr_value = node.attributes.get(attribute)
                if attr_value:
                    results.append(attr_value)
        
        if results:
            return "\n".join(results)
        else:
            return f"No se pudo extraer el atributo '{attribute}' de los elementos encontrados."

    except ImportError:
        return "Error: Las librerías 'httpx' y 'selectolax' no están instaladas. Por favor, instálalas con 'pip install httpx selectolax'."
    except httpx.RequestError as e:
        return f"Error de conexión al acceder a la URL: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al acceder a la URL: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al extraer información de la web: {e}"
