PLUGIN_NAME = "base64"
PLUGIN_DESCRIPTION = "Codifica y decodifica texto o archivos en formato Base64."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "base64",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (encode_text, decode_text, encode_file, decode_file)",
                    "enum": ["encode_text", "decode_text", "encode_file", "decode_file"]
                },
                "data": {
                    "type": "string",
                    "description": "Texto a codificar/decodificar (requerido para encode_text, decode_text)"
                },
                "file_path": {
                    "type": "string",
                    "description": "Ruta al archivo a codificar/decodificar (requerido para encode_file, decode_file)"
                },
                "output_file_path": {
                    "type": "string",
                    "description": "Ruta donde guardar el archivo resultante (opcional para encode_file, decode_file)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, data: str = None, file_path: str = None, output_file_path: str = None) -> str:
    import base64
    import os

    try:
        if action == "encode_text":
            if not data: return "Error: Se requiere texto para codificar."
            encoded_bytes = base64.b64encode(data.encode("utf-8"))
            return encoded_bytes.decode("utf-8")
        elif action == "decode_text":
            if not data: return "Error: Se requiere texto Base64 para decodificar."
            decoded_bytes = base64.b64decode(data.encode("utf-8"))
            return decoded_bytes.decode("utf-8")
        elif action == "encode_file":
            if not file_path: return "Error: Se requiere la ruta del archivo para codificar."
            if not os.path.exists(file_path): return f"Error: El archivo {file_path} no existe."
            with open(file_path, "rb") as f:
                encoded_content = base64.b64encode(f.read())
            if output_file_path:
                with open(output_file_path, "wb") as f_out:
                    f_out.write(encoded_content)
                return f"Archivo {file_path} codificado en Base64 y guardado en {output_file_path}."
            else:
                return encoded_content.decode("utf-8")
        elif action == "decode_file":
            if not file_path: return "Error: Se requiere la ruta del archivo Base64 para decodificar."
            if not os.path.exists(file_path): return f"Error: El archivo {file_path} no existe."
            with open(file_path, "rb") as f:
                decoded_content = base64.b64decode(f.read())
            if output_file_path:
                with open(output_file_path, "wb") as f_out:
                    f_out.write(decoded_content)
                return f"Archivo {file_path} decodificado de Base64 y guardado en {output_file_path}."
            else:
                return decoded_content.decode("utf-8")
        else:
            return "Acción de Base64 no reconocida."
    except Exception as e:
        return f"Error en el plugin Base64: {e}"
