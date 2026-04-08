PLUGIN_NAME = "barcode"
PLUGIN_DESCRIPTION = "Genera y lee códigos de barras (EAN-13, Code 128, QR, etc.)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "barcode",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (generate, read)",
                    "enum": ["generate", "read"]
                },
                "data": {
                    "type": "string",
                    "description": "Datos para generar el código de barras (requerido para generate)"
                },
                "barcode_type": {
                    "type": "string",
                    "description": "Tipo de código de barras a generar (ej. EAN13, Code128, QR)",
                    "default": "EAN13"
                },
                "filename": {
                    "type": "string",
                    "description": "Nombre del archivo de imagen a guardar (ej. my_barcode.png)",
                    "default": "barcode.png"
                },
                "image_path": {
                    "type": "string",
                    "description": "Ruta a la imagen del código de barras para leer (requerido para read)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, data: str = None, barcode_type: str = "EAN13", filename: str = "barcode.png", image_path: str = None) -> str:
    try:
        if action == "generate":
            if not data:
                return "Error: Se requieren datos para generar el código de barras."
            if barcode_type.upper() == "QR":
                import qrcode
                img = qrcode.make(data)
                img.save(filename)
                return f"Código QR generado y guardado como {filename}"
            else:
                from barcode import EAN13, Code128
                from barcode.writer import ImageWriter
                if barcode_type.upper() == "EAN13":
                    # EAN13 requiere 12 o 13 dígitos numéricos
                    if not data.isdigit() or len(data) not in [12, 13]:
                        return "Error: EAN13 requiere 12 o 13 dígitos numéricos."
                    barcode_class = EAN13
                elif barcode_type.upper() == "CODE128":
                    barcode_class = Code128
                else:
                    return f"Error: Tipo de código de barras '{barcode_type}' no soportado para generación (solo EAN13, Code128, QR)."
                
                # Generar el código de barras y guardarlo como imagen
                with open(filename, "wb") as f:
                    barcode_class(data, writer=ImageWriter()).write(f)
                return f"Código de barras {barcode_type} generado y guardado como {filename}"
        elif action == "read":
            if not image_path:
                return "Error: Se requiere la ruta de la imagen para leer el código de barras."
            from pyzbar.pyzbar import decode
            from PIL import Image
            
            img = Image.open(image_path)
            decoded_objects = decode(img)
            
            if decoded_objects:
                results = []
                for obj in decoded_objects:
                    results.append(f"Tipo: {obj.type}, Datos: {obj.data.decode('utf-8')}")
                return "\n".join(results)
            else:
                return "No se detectaron códigos de barras en la imagen."
        else:
            return "Acción de código de barras no reconocida."
    except ImportError:
        return "Error: Las librerías necesarias (barcode, qrcode, pyzbar, Pillow) no están instaladas. Por favor, instálalas con \"pip install python-barcode qrcode pyzbar Pillow\"."
    except FileNotFoundError:
        return f"Error: El archivo de imagen en la ruta {image_path} no fue encontrado."
    except Exception as e:
        return f"Error al procesar el código de barras: {e}"
