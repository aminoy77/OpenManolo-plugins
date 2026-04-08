PLUGIN_NAME = "meme"
PLUGIN_DESCRIPTION = "Genera memes de texto con plantillas predefinidas."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "meme",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "top_text": {"type": "string", "description": "Texto superior del meme"},
                "bottom_text": {"type": "string", "description": "Texto inferior del meme"},
                "template": {
                    "type": "string",
                    "description": "Plantilla de meme (ej. 'distracted_boyfriend', 'drake_hotline_bling'). Por defecto: 'impact'.",
                    "default": "impact"
                }
            },
            "required": ["top_text", "bottom_text"]
        }
    }
}

def run(top_text: str, bottom_text: str, template: str = "impact") -> str:
    # En un entorno real, esto se integraría con una API de generación de memes (ej. Imgflip API)
    # o una librería de procesamiento de imágenes como Pillow para superponer texto en plantillas.
    # Aquí se simula la generación del meme.
    return f"Meme generado con plantilla '{template}':\nTexto superior: {top_text}\nTexto inferior: {bottom_text}\n(Simulado: la imagen real no se genera aquí)"
