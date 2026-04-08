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
        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convertir a Mbps
        upload_speed = st.upload() / 1_000_000    # Convertir a Mbps
        ping = st.results.ping

        return f"Test de velocidad de internet:\nDescarga: {download_speed:.2f} Mbps\nSubida: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms"
    except ImportError:
        return "Error: La librería \'speedtest-cli\' no está instalada. Por favor, instálala con \'pip install speedtest-cli\'."
    except Exception as e:
        return f"Error al realizar el test de velocidad: {e}"
