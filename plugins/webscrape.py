PLUGIN_NAME = "webscrape"
PLUGIN_DESCRIPTION = "Extrae el texto principal de una página web, eliminando elementos de navegación y publicidad."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "webscrape",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "La URL de la página web a extraer"}
            },
            "required": ["url"]
        }
    }
}

def run(url: str) -> str:
    try:
        import httpx
        from bs4 import BeautifulSoup

        response = httpx.get(url, timeout=15)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos

        soup = BeautifulSoup(response.text, "html.parser")

        # Eliminar scripts, estilos, navegación, headers, footers, etc.
        for unwanted_tag in soup(["script", "style", "nav", "header", "footer", "aside", "form", "img", "svg", "canvas"]):
            unwanted_tag.decompose()

        # Extraer texto de los elementos principales del contenido
        main_content_tags = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "blockquote"])
        text_content = "\n".join([tag.get_text(separator=" ", strip=True) for tag in main_content_tags if tag.get_text(strip=True)])

        if not text_content:
            # Fallback si no se encuentra contenido principal estructurado
            text_content = soup.get_text(separator=" ", strip=True)

        # Limpiar múltiples espacios en blanco y saltos de línea
        import re
        text_content = re.sub(r"\s+", " ", text_content).strip()
        text_content = re.sub(r"\n\s*\n", "\n\n", text_content).strip()

        return text_content[:4000] + ("..." if len(text_content) > 4000 else "")
    except httpx.RequestError as e:
        return f"Error de conexión al acceder a la URL: {e}"
    except Exception as e:
        return f"Error al extraer contenido de la web: {e}"
