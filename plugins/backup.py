PLUGIN_NAME = "backup"
PLUGIN_DESCRIPTION = "Crea copias de seguridad de directorios, comprimiéndolos en un archivo ZIP o TAR.GZ."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "backup",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "source_path": {"type": "string", "description": "Ruta del directorio a respaldar"},
                "destination_path": {"type": "string", "description": "Ruta donde se guardará el archivo de respaldo"},
                "format": {
                    "type": "string",
                    "description": "Formato del archivo de respaldo (zip, tar.gz)",
                    "enum": ["zip", "tar.gz"],
                    "default": "zip"
                }
            },
            "required": ["source_path", "destination_path"]
        }
    }
}

def run(source_path: str, destination_path: str, format: str = "zip") -> str:
    import shutil
    import os
    import datetime

    try:
        if not os.path.isdir(source_path):
            return f"Error: La ruta de origen {source_path} no es un directorio válido."

        # Crear el directorio de destino si no existe
        os.makedirs(destination_path, exist_ok=True)

        # Generar nombre de archivo de respaldo con timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.basename(source_path)
        archive_name = os.path.join(destination_path, f"{base_name}_{timestamp}")

        if format == "zip":
            shutil.make_archive(archive_name, "zip", root_dir=os.path.dirname(source_path), base_dir=base_name)
            return f"Copia de seguridad de {source_path} creada en {archive_name}.zip"
        elif format == "tar.gz":
            shutil.make_archive(archive_name, "gztar", root_dir=os.path.dirname(source_path), base_dir=base_name)
            return f"Copia de seguridad de {source_path} creada en {archive_name}.tar.gz"
        else:
            return "Error: Formato de respaldo no soportado. Use \"zip\" o \"tar.gz\"."

    except Exception as e:
        return f"Error al crear la copia de seguridad: {e}"
