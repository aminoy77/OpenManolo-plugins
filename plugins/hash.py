PLUGIN_NAME = "hash"
PLUGIN_DESCRIPTION = "Genera hashes criptográficos (MD5, SHA256) de un texto."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "hash",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "El texto a hashear"},
                "algorithm": {"type": "string", "enum": ["md5", "sha256"], "description": "Algoritmo de hashing (md5 o sha256)", "default": "sha256"}
            },
            "required": ["text"]
        }
    }
}

def run(text: str, algorithm: str = "sha256") -> str:
    import hashlib
    try:
        if algorithm == "md5":
            return hashlib.md5(text.encode()).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(text.encode()).hexdigest()
        else:
            return f"Error: Algoritmo ‘{algorithm}’ no soportado. Usa ‘md5’ o ‘sha256’."
    except Exception as e:
        return f"Error al generar el hash: {e}"
