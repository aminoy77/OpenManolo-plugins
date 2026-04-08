PLUGIN_NAME = "color"
PLUGIN_DESCRIPTION = "Convierte colores entre diferentes formatos (hex, rgb, hsl, nombre)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "color",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "input_color": {"type": "string", "description": "El color de entrada (ej. #FF0000, rgb(255,0,0), red)"},
                "target_format": {
                    "type": "string",
                    "description": "Formato de salida deseado (hex, rgb, hsl, name)",
                    "enum": ["hex", "rgb", "hsl", "name"]
                }
            },
            "required": ["input_color", "target_format"]
        }
    }
}

def run(input_color: str, target_format: str) -> str:
    try:
        from webcolors import hex_to_rgb, rgb_to_hex, rgb_to_name, name_to_rgb
        from colorsys import rgb_to_hls, hls_to_rgb

        r, g, b = 0, 0, 0

        # Convertir a RGB (base para todas las conversiones)
        if input_color.startswith("#"):
            r, g, b = hex_to_rgb(input_color)
        elif input_color.startswith("rgb("):
            parts = input_color.replace("rgb(", "").replace(")", "").split(",")
            r, g, b = int(parts[0]), int(parts[1]), int(parts[2])
        elif input_color.isalpha():
            try:
                r, g, b = name_to_rgb(input_color.lower())
            except ValueError:
                return f"Error: Nombre de color \'{input_color}\' no reconocido."
        else:
            return "Error: Formato de color de entrada no reconocido. Use HEX, RGB o nombre de color."

        # Convertir a formato de salida
        if target_format == "hex":
            return rgb_to_hex((r, g, b))
        elif target_format == "rgb":
            return f"rgb({r},{g},{b})"
        elif target_format == "hsl":
            h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
            return f"hsl({int(h * 360)}, {int(s * 100)}%, {int(l * 100)}%)"
        elif target_format == "name":
            try:
                return rgb_to_name((r, g, b))
            except ValueError:
                return f"No hay un nombre de color exacto para rgb({r},{g},{b})."
        else:
            return "Error: Formato de salida no reconocido. Use hex, rgb, hsl o name."

    except ImportError:
        return "Error: La librería \'webcolors\' no está instalada. Por favor, instálala con \'pip install webcolors\'."
    except Exception as e:
        return f"Error al convertir el color: {e}"
