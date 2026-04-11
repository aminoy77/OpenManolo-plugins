PLUGIN_NAME = "movie"
PLUGIN_DESCRIPTION = "Busca información detallada de películas y series (sinopsis, reparto, puntuación) utilizando la OMDb API."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "movie",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Título de la película o serie a buscar"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str) -> str:
    try:
        import httpx

        # NOTA: La OMDb API requiere una clave API. Puedes obtener una gratuita en http://www.omdbapi.com/apikey.aspx
        # Por ahora, usaremos un placeholder. En un entorno real, deberías usar una variable de entorno.
        OMDB_API_KEY = "YOUR_OMDB_API_KEY" # Reemplaza con tu clave API real

        if OMDB_API_KEY == "YOUR_OMDB_API_KEY":
            return "ERROR: La OMDb API Key no está configurada. Obtén una en http://www.omdbapi.com/apikey.aspx y actualiza el plugin."

        api_url = f"http://www.omdbapi.com/?t={query}&apikey={OMDB_API_KEY}&plot=full&r=json"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if data.get("Response") == "False":
            return f"Error: No se encontró información para \'{query}\'. Mensaje de OMDb: {data.get("Error", "Desconocido")}"

        output = [
            f"Título: {data.get("Title", "N/A")} ({data.get("Year", "N/A")})",
            f"Tipo: {data.get("Type", "N/A").capitalize()}",
            f"Director: {data.get("Director", "N/A")}",
            f"Actores: {data.get("Actors", "N/A")}",
            f"Género: {data.get("Genre", "N/A")}",
            f"Sinopsis: {data.get("Plot", "N/A")}",
            f"IMDb Rating: {data.get("imdbRating", "N/A")}",
            f"Premios: {data.get("Awards", "N/A")}"
        ]
        return "\n".join(output)
    except httpx.RequestError as e:
        return f"Error de conexión al API de OMDb: {e}"
    except Exception as e:
        return f"Error al buscar información de películas/series: {e}"
