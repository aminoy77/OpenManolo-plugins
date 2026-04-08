PLUGIN_NAME = "instagram"
PLUGIN_DESCRIPTION = "Obtiene información básica de perfiles públicos de Instagram (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "instagram",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {"type": "string", "description": "Nombre de usuario de Instagram"}
            },
            "required": ["username"]
        }
    }
}

def run(username: str) -> str:
    # La API de Instagram es muy restrictiva para perfiles públicos y requiere autenticación.
    # El scraping es difícil y a menudo bloqueado. Por lo tanto, esta funcionalidad será simulada.
    return f"Buscando información del perfil de Instagram @{username}. Resultados simulados: Seguidores: 1.2M, Publicaciones: 345, Biografía: 'Creador de contenido'."
