PLUGIN_NAME = "password"
PLUGIN_DESCRIPTION = "Genera contraseñas seguras y aleatorias con opciones de longitud y caracteres."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "password",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "length": {"type": "integer", "description": "Longitud de la contraseña (mínimo 8, máximo 64)", "default": 16},
                "include_digits": {"type": "boolean", "description": "Incluir números (0-9)", "default": True},
                "include_symbols": {"type": "boolean", "description": "Incluir símbolos (!@#$%^&*())", "default": True},
                "include_uppercase": {"type": "boolean", "description": "Incluir letras mayúsculas (A-Z)", "default": True},
                "include_lowercase": {"type": "boolean", "description": "Incluir letras minúsculas (a-z)", "default": True}
            },
            "required": []
        }
    }
}

def run(length: int = 16, include_digits: bool = True, include_symbols: bool = True, include_uppercase: bool = True, include_lowercase: bool = True) -> str:
    import secrets
    import string

    if length < 8 or length > 64:
        return "Error: La longitud de la contraseña debe estar entre 8 y 64 caracteres."

    characters = ""
    if include_digits: characters += string.digits
    if include_symbols: characters += string.punctuation
    if include_uppercase: characters += string.ascii_uppercase
    if include_lowercase: characters += string.ascii_lowercase

    if not characters:
        return "Error: Debes seleccionar al menos un tipo de carácter para generar la contraseña."

    try:
        password = 
''.join(secrets.choice(characters) for _ in range(length))
        return f"Contraseña generada: {password}"
    except Exception as e:
        return f"Error al generar la contraseña: {e}"
