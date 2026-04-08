PLUGIN_NAME = "pdf"
PLUGIN_DESCRIPTION = "Lee y extrae texto de archivos PDF."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pdf",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Ruta al archivo PDF"},
                "page_number": {"type": "integer", "description": "Número de página a extraer (opcional, si no se especifica, extrae todo)"}
            },
            "required": ["file_path"]
        }
    }
}

def run(file_path: str, page_number: int = None) -> str:
    try:
        from pypdf import PdfReader
        reader = PdfReader(file_path)
        if page_number is not None:
            if 0 < page_number <= len(reader.pages):
                page = reader.pages[page_number - 1] # pypdf es 0-indexado
                return page.extract_text()
            else:
                return f"Error: Número de página inválido. El PDF tiene {len(reader.pages)} páginas."
        else:
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except ImportError:
        return "Error: La librería \'pypdf\' no está instalada. Por favor, instálala con \'pip install pypdf\'."
    except FileNotFoundError:
        return f"Error: El archivo PDF en la ruta {file_path} no fue encontrado."
    except Exception as e:
        return f"Error al leer el archivo PDF: {e}"
