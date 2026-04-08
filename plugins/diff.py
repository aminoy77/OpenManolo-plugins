PLUGIN_NAME = "diff"
PLUGIN_DESCRIPTION = "Compara las diferencias entre dos archivos de texto o dos cadenas de texto."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "diff",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (text_diff, file_diff)",
                    "enum": ["text_diff", "file_diff"]
                },
                "text1": {
                    "type": "string",
                    "description": "Primer texto a comparar (requerido para text_diff)"
                },
                "text2": {
                    "type": "string",
                    "description": "Segundo texto a comparar (requerido para text_diff)"
                },
                "file_path1": {
                    "type": "string",
                    "description": "Ruta del primer archivo a comparar (requerido para file_diff)"
                },
                "file_path2": {
                    "type": "string",
                    "description": "Ruta del segundo archivo a comparar (requerido para file_diff)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, text1: str = None, text2: str = None, file_path1: str = None, file_path2: str = None) -> str:
    import difflib
    import os

    try:
        if action == "text_diff":
            if text1 is None or text2 is None: return "Error: Se requieren dos textos para comparar."
            diff = difflib.unified_diff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
            return "".join(diff)
        elif action == "file_diff":
            if file_path1 is None or file_path2 is None: return "Error: Se requieren dos rutas de archivo para comparar."
            if not os.path.exists(file_path1): return f"Error: El archivo {file_path1} no existe."
            if not os.path.exists(file_path2): return f"Error: El archivo {file_path2} no existe."

            with open(file_path1, "r", encoding="utf-8") as f1:
                content1 = f1.readlines()
            with open(file_path2, "r", encoding="utf-8") as f2:
                content2 = f2.readlines()

            diff = difflib.unified_diff(content1, content2, fromfile=file_path1, tofile=file_path2)
            return "".join(diff)
        else:
            return "Acción de diff no reconocida."
    except Exception as e:
        return f"Error en el plugin Diff: {e}"
