PLUGIN_NAME = "base64encode"
PLUGIN_DESCRIPTION = "Codifica y decodifica texto en Base64."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "base64encode",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["encode", "decode"], "description": "Acción a realizar (encode o decode)"},
                "text": {"type": "string", "description": "El texto a codificar o decodificar"}
            },
            "required": ["action", "text"]
        }
    }
}

def run(action: str, text: str) -> str:
    import base64
    try:
        if action == "encode":
            encoded_bytes = base64.b64encode(text.encode("utf-8"))
            return encoded_bytes.decode("utf-8")
        elif action == "decode":
            decoded_bytes = base64.b64decode(text.encode("utf-8"))
            return decoded_bytes.decode("utf-8")
        else:
            return f"Error: Acción ‘{action}’ no soportada. Usa ‘encode’ o ‘decode’."
    except Exception as e:
        return f"Error al realizar la operación Base64: {e}"
