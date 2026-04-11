PLUGIN_NAME = "sysinfo"
PLUGIN_DESCRIPTION = "Obtiene información detallada del sistema operativo y hardware."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "sysinfo",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

def run() -> str:
    try:
        import psutil
        import platform

        info = []

        # Sistema operativo
        info.append(f"Sistema Operativo: {platform.system()} {platform.release()} ({platform.version()})")
        info.append(f"Arquitectura: {platform.machine()}")
        info.append(f"Nombre del Host: {platform.node()}")

        # CPU
        info.append(f"\n--- CPU ---")
        info.append(f"Procesador: {platform.processor()}")
        info.append(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
        info.append(f"Núcleos Totales (Lógicos): {psutil.cpu_count(logical=True)}")
        info.append(f"Uso de CPU: {psutil.cpu_percent(interval=1)}%")

        # Memoria
        info.append(f"\n--- Memoria ---")
        svmem = psutil.virtual_memory()
        info.append(f"Total: {svmem.total / (1024**3):.2f} GB")
        info.append(f"Disponible: {svmem.available / (1024**3):.2f} GB")
        info.append(f"Usada: {svmem.used / (1024**3):.2f} GB")
        info.append(f"Porcentaje: {svmem.percent}%")

        # Disco
        info.append(f"\n--- Disco ---")
        partitions = psutil.disk_partitions()
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                info.append(f"  Dispositivo: {p.device}")
                info.append(f"    Punto de Montaje: {p.mountpoint}")
                info.append(f"    Sistema de Archivos: {p.fstype}")
                info.append(f"    Total: {usage.total / (1024**3):.2f} GB")
                info.append(f"    Usado: {usage.used / (1024**3):.2f} GB")
                info.append(f"    Libre: {usage.free / (1024**3):.2f} GB")
                info.append(f"    Porcentaje: {usage.percent}%")
            except PermissionError:
                continue

        # Red
        info.append(f"\n--- Red ---")
        net_io = psutil.net_io_counters()
        info.append(f"Bytes Enviados: {net_io.bytes_sent / (1024**2):.2f} MB")
        info.append(f"Bytes Recibidos: {net_io.bytes_recv / (1024**2):.2f} MB")

        return "\n".join(info)
    except ImportError:
        return "ERROR: La librería \'psutil\' no está instalada. Ejecuta: pip3 install psutil --break-system-packages"
    except Exception as e:
        return f"Error al obtener información del sistema: {e}"
