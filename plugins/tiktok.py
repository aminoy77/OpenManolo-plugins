PLUGIN_NAME = "tiktok"
PLUGIN_DESCRIPTION = "Busca vídeos trending o por hashtag en TikTok (simulado)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "tiktok",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (trending_videos, search_hashtag)",
                    "enum": ["trending_videos", "search_hashtag"]
                },
                "hashtag": {
                    "type": "string",
                    "description": "Hashtag a buscar (requerido para search_hashtag)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, hashtag: str = None) -> str:
    # La API de TikTok es muy restrictiva y el scraping es complejo.
    # Por lo tanto, esta funcionalidad será simulada.
    if action == "trending_videos":
        return "Vídeos trending de TikTok (simulado): Video 1: Baile viral, Video 2: Reto divertido, Video 3: Tutorial rápido."
    elif action == "search_hashtag":
        if not hashtag:
            return "Error: Se requiere un hashtag para buscar vídeos."
        return f"Buscando vídeos en TikTok con el hashtag #{hashtag}. Resultados simulados: Vídeo A, Vídeo B, Vídeo C."
    else:
        return "Acción de TikTok no válida. Use \'trending_videos\' o \'search_hashtag\'."
