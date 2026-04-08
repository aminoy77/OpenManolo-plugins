PLUGIN_NAME = "imagegen"
PLUGIN_DESCRIPTION = "Genera prompts detallados para modelos de IA de generación de imágenes (ej. DALL-E, Midjourney, Stable Diffusion)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "imagegen",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "subject": {"type": "string", "description": "El sujeto principal de la imagen"},
                "style": {"type": "string", "description": "Estilo artístico (ej. fotorrealista, acuarela, cyberpunk, impresionista)", "default": "fotorrealista"},
                "details": {"type": "string", "description": "Detalles adicionales (iluminación, composición, colores, ambiente)", "default": ""}
            },
            "required": ["subject"]
        }
    }
}

def run(subject: str, style: str = "fotorrealista", details: str = "") -> str:
    prompt = f"Genera una imagen de {subject} en un estilo {style}."
    if details:
        prompt += f" Detalles adicionales: {details}."
    prompt += " --ar 16:9 --v 5.2"
    return f"Prompt generado para IA de imágenes: \n\"{prompt}\"
(Este plugin solo genera el prompt, no la imagen.)"
