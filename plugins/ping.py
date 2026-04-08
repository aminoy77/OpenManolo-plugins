PLUGIN_NAME = "ping"
PLUGIN_DESCRIPTION = "Realiza un ping a una dirección IP o nombre de host para comprobar la conectividad."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "ping",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "host": {"type": "string", "description": "Dirección IP o nombre de host a hacer ping"},
                "count": {"type": "integer", "description": "Número de pings a enviar", "default": 4}
            },
            "required": ["host"]
        }
    }
}

def run(host: str, count: int = 4) -> str:
    import subprocess
    import platform

    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), host]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, timeout=10)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error al hacer ping a {host}: {e.stderr}"
    except subprocess.TimeoutExpired:
        return f"Tiempo de espera agotado al hacer ping a {host}."
    except FileNotFoundError:
        return "Error: El comando ping no se encontró. Asegúrate de que esté instalado y en el PATH."
    except Exception as e:
        return f"Error inesperado al hacer ping: {e}"
