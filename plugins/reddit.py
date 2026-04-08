PLUGIN_NAME = "reddit"
PLUGIN_DESCRIPTION = "Busca posts y comentarios en Reddit por palabra clave o subreddit (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "reddit",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Término de búsqueda"},
                "subreddit": {"type": "string", "description": "Subreddit específico (opcional)"},
                "type": {"type": "string", "description": "Tipo de búsqueda (posts, comments)", "enum": ["posts", "comments"], "default": "posts"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str, subreddit: str = None, type: str = "posts") -> str:
    # La API de Reddit (PRAW) requiere autenticación y configuración.
    # Por lo tanto, esta funcionalidad será simulada.
    if type == "posts":
        if subreddit:
            return f"Buscando posts sobre \'{query}\' en r/{subreddit}. Resultados simulados: Post 1, Post 2."
        else:
            return f"Buscando posts sobre \'{query}\' en Reddit. Resultados simulados: Post 1, Post 2."
    elif type == "comments":
        if subreddit:
            return f"Buscando comentarios sobre \'{query}\' en r/{subreddit}. Resultados simulados: Comentario A, Comentario B."
        else:
            return f"Buscando comentarios sobre \'{query}\' en Reddit. Resultados simulados: Comentario A, Comentario B."
    else:
        return "Tipo de búsqueda no válido. Use \'posts\' o \'comments\'."
