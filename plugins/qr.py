PLUGIN_NAME = "qr"
PLUGIN_DESCRIPTION = "Genera un código QR a partir de un texto o URL y lo guarda como imagen."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "qr",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "El texto o URL para codificar en el QR"},
                "filename": {"type": "string", "description": "Nombre del archivo de imagen a guardar (ej. \'mi_qr.png\'). Por defecto es \'qrcode.png\'.", "default": "qrcode.png"}
            },
            "required": ["data"]
        }
    }
}

def run(data: str, filename: str = "qrcode.png") -> str:
    try:
        import qrcode
        from pathlib import Path

        # Crear el objeto QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen en el directorio de trabajo
        save_path = Path.cwd() / filename
        img.save(save_path)

        return f"Código QR generado y guardado en: {save_path}"
    except ImportError:
        return "ERROR: La librería \'qrcode\' no está instalada. Ejecuta: pip3 install qrcode --break-system-packages"
    except Exception as e:
        return f"Error al generar el código QR: {e}"
