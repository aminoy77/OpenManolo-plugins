PLUGIN_NAME = "speedtest"
PLUGIN_DESCRIPTION = "Realiza un test de velocidad de internet (descarga, subida y ping)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "speedtest",
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
        import subprocess
        import json

        # Ejecutar speedtest-cli en modo JSON
        command = ["speedtest", "--json"]
        process = subprocess.run(command, capture_output=True, text=True, check=True, timeout=60)
        
        data = json.loads(process.stdout)

        download_mbps = data["download"] / 1_000_000
        upload_mbps = data["upload"] / 1_000_000
        ping_ms = data["ping"]
        server_name = data["server"]["name"]
        server_sponsor = data["server"]["sponsor"]

        return (
            f"Test de Velocidad de Internet:\n"
            f"  Servidor: {server_name} ({server_sponsor})\n"
            f"  Descarga: {download_mbps:.2f} Mbps\n"
            f"  Subida: {upload_mbps:.2f} Mbps\n"
            f"  Ping: {ping_ms:.2f} ms"
        )
    except FileNotFoundError:
        return "ERROR: El comando \'speedtest\' no se encontró. Asegúrate de que speedtest-cli esté instalado (pip3 install speedtest-cli --break-system-packages)."
    except subprocess.CalledProcessError as e:
        return f"ERROR: speedtest-cli falló con código {e.returncode}. Salida: {e.stderr}"
    except subprocess.TimeoutExpired:
        return "ERROR: El test de velocidad excedió el tiempo límite (60 segundos)."
    except json.JSONDecodeError:
        return "ERROR: No se pudo parsear la salida JSON de speedtest-cli."
    except Exception as e:
        return f"Error al realizar el test de velocidad: {e}"
