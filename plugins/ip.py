PLUGIN_NAME = "ip"
PLUGIN_DESCRIPTION = "Obtiene información detallada de una dirección IP pública, incluyendo geolocalización."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "ip",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "ip_address": {"type": "string", "description": "La dirección IP a consultar (opcional, si se omite, usa la IP pública del agente)", "default": ""}
            },
            "required": []
        }
    }
}

def run(ip_address: str = "") -> str:
    try:
        import httpx

        if not ip_address:
            api_url = "https://ipapi.co/json/"
        else:
            api_url = f"https://ipapi.co/{ip_address}/json/"

        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if data.get("error"):
            return f"Error al consultar IP {ip_address}: {data.get("reason", "Error desconocido")}"

        output = [
            f"Información para IP: {data.get("ip", "N/A")}",
            f"Ciudad: {data.get("city", "N/A")}",
            f"Región: {data.get("region", "N/A")}",
            f"País: {data.get("country_name", "N/A")} ({data.get("country_code", "N/A")})",
            f"Latitud: {data.get("latitude", "N/A")}",
            f"Longitud: {data.get("longitude", "N/A")}",
            f"Organización: {data.get("org", "N/A")}",
            f"ASN: {data.get("asn", "N/A")}",
            f"Zona Horaria: {data.get("timezone", "N/A")}"
        ]
        return "\n".join(output)
    except httpx.RequestError as e:
        return f"Error de conexión al API de IP: {e}"
    except Exception as e:
        return f"Error al obtener información de IP: {e}"
