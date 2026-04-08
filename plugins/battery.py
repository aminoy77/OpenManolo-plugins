PLUGIN_NAME = "battery"
PLUGIN_DESCRIPTION = "Obtiene información detallada de la batería (nivel, estado, tiempo restante) en laptops."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "battery",
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
        battery = psutil.sensors_battery()
        if battery:
            plugged = "Sí" if battery.power_plugged else "No"
            percent = battery.percent
            secsleft = battery.secsleft

            if secsleft == psutil.POWER_TIME_UNLIMITED:
                time_left = "Ilimitado"
            elif secsleft == psutil.POWER_TIME_UNKNOWN:
                time_left = "Desconocido"
            else:
                minutes, seconds = divmod(secsleft, 60)
                hours, minutes = divmod(minutes, 60)
                time_left = f"{int(hours)}h {int(minutes)}m"

            return f"Información de la batería:\nNivel: {percent}%\nCargando: {plugged}\nTiempo restante: {time_left}"
        else:
            return "No se detectó batería o no es una laptop."
    except ImportError:
        return "Error: La librería \'psutil\' no está instalada. Por favor, instálala con \'pip install psutil\'."
    except Exception as e:
        return f"Error inesperado al obtener información de la batería: {e}"
