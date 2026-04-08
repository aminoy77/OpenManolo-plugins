PLUGIN_NAME = "sslcheck"
PLUGIN_DESCRIPTION = "Verifica el certificado SSL/TLS de un dominio, mostrando su validez y fecha de expiración."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "sslcheck",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "El dominio a verificar (ej. google.com)"},
                "port": {"type": "integer", "description": "Puerto para la conexión SSL (normalmente 443)", "default": 443}
            },
            "required": ["domain"]
        }
    }
}

def run(domain: str, port: int = 443) -> str:
    import ssl
    import socket
    import datetime

    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        # Extraer fechas de validez
        not_before = datetime.datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z")
        not_after = datetime.datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        
        # Calcular días restantes
        days_remaining = (not_after - datetime.datetime.now()).days

        output = f"Certificado SSL para {domain}:\n"
        output += f"  Emisor: {cert["issuer"][0][0][1]}\n"
        output += f"  Sujeto: {cert["subject"][0][0][1]}\n"
        output += f"  Válido desde: {not_before.strftime("%Y-%m-%d %H:%M:%S")}\n"
        output += f"  Válido hasta: {not_after.strftime("%Y-%m-%d %H:%M:%S")}\n"
        output += f"  Días restantes: {days_remaining}\n"
        output += f"  Estado: {'Válido' if days_remaining > 0 else 'Expirado o por expirar'}"
        
        return output

    except socket.gaierror:
        return f"Error: No se pudo resolver el dominio \'{domain}\"."
    except ConnectionRefusedError:
        return f"Error: Conexión rechazada al puerto {port} en {domain}."
    except ssl.SSLError as e:
        return f"Error SSL: {e}. Asegúrate de que el dominio usa HTTPS y el puerto es correcto."
    except Exception as e:
        return f"Error inesperado al verificar el certificado SSL: {e}"
