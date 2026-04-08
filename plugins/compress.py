PLUGIN_NAME = "compress"
PLUGIN_DESCRIPTION = "Comprime y descomprime archivos o directorios en formatos como ZIP o TAR.GZ."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "compress",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (compress, decompress)",
                    "enum": ["compress", "decompress"]
                },
                "input_path": {
                    "type": "string",
                    "description": "Ruta al archivo/directorio de entrada para comprimir o al archivo comprimido para descomprimir"
                },
                "output_path": {
                    "type": "string",
                    "description": "Ruta donde guardar el archivo/directorio resultante"
                },
                "format": {
                    "type": "string",
                    "description": "Formato de compresión (zip, tar.gz)",
                    "enum": ["zip", "tar.gz"],
                    "default": "zip"
                }
            },
            "required": ["action", "input_path", "output_path"]
        }
    }
}

def run(action: str, input_path: str, output_path: str, format: str = "zip") -> str:
    import shutil
    import os

    try:
        if action == "compress":
            if not os.path.exists(input_path):
                return f"Error: La ruta de entrada {input_path} no existe."
            if os.path.isdir(input_path):
                base_name = os.path.basename(input_path)
                archive_name = os.path.join(output_path, base_name)
                if format == "zip":
                    shutil.make_archive(archive_name, "zip", root_dir=os.path.dirname(input_path), base_dir=base_name)
                    return f"Directorio {input_path} comprimido en {archive_name}.zip"
                elif format == "tar.gz":
                    shutil.make_archive(archive_name, "gztar", root_dir=os.path.dirname(input_path), base_dir=base_name)
                    return f"Directorio {input_path} comprimido en {archive_name}.tar.gz"
                else:
                    return "Formato de compresión no soportado para directorios."
            elif os.path.isfile(input_path):
                return "Error: La compresión de archivos individuales directamente no está implementada para este plugin. Comprime el directorio que lo contiene."
            else:
                return "Error: La ruta de entrada no es un archivo ni un directorio válido."
        elif action == "decompress":
            if not os.path.exists(input_path):
                return f"Error: El archivo comprimido {input_path} no existe."
            if format == "zip":
                shutil.unpack_archive(input_path, output_path, "zip")
                return f"Archivo {input_path} descomprimido en {output_path}"
            elif format == "tar.gz":
                shutil.unpack_archive(input_path, output_path, "gztar")
                return f"Archivo {input_path} descomprimido en {output_path}"
            else:
                return "Formato de descompresión no soportado."
        else:
            return "Acción de compresión no reconocida."
    except Exception as e:
        return f"Error en el plugin Compress: {e}"
