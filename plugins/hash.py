PLUGIN_NAME = "hash"
PLUGIN_DESCRIPTION = "Genera hashes criptográficos (MD5, SHA1, SHA256, SHA512) de texto o archivos."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "hash",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (hash_text, hash_file)",
                    "enum": ["hash_text", "hash_file"]
                },
                "data": {
                    "type": "string",
                    "description": "Texto a hashear (requerido para hash_text)"
                },
                "file_path": {
                    "type": "string",
                    "description": "Ruta al archivo a hashear (requerido para hash_file)"
                },
                "hash_type": {
                    "type": "string",
                    "description": "Tipo de hash a generar (md5, sha1, sha256, sha512)",
                    "enum": ["md5", "sha1", "sha256", "sha512"],
                    "default": "sha256"
                }
            },
            "required": ["action", "hash_type"]
        }
    }
}

def run(action: str, hash_type: str, data: str = None, file_path: str = None) -> str:
    import hashlib
    import os

    try:
        hasher = None
        if hash_type == "md5":
            hasher = hashlib.md5()
        elif hash_type == "sha1":
            hasher = hashlib.sha1()
        elif hash_type == "sha256":
            hasher = hashlib.sha256()
        elif hash_type == "sha512":
            hasher = hashlib.sha512()
        else:
            return "Error: Tipo de hash no soportado. Use md5, sha1, sha256 o sha512."

        if action == "hash_text":
            if not data: return "Error: Se requiere texto para hashear."
            hasher.update(data.encode("utf-8"))
            return hasher.hexdigest()
        elif action == "hash_file":
            if not file_path: return "Error: Se requiere la ruta del archivo para hashear."
            if not os.path.exists(file_path): return f"Error: El archivo {file_path} no existe."
            with open(file_path, "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            return hasher.hexdigest()
        else:
            return "Acción de hash no reconocida."
    except Exception as e:
        return f"Error en el plugin Hash: {e}"
