PLUGIN_NAME = "dnslookup"
PLUGIN_DESCRIPTION = "Realiza consultas DNS para obtener información como direcciones IP, registros MX, NS, etc."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "dnslookup",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "hostname": {"type": "string", "description": "El nombre de host o dominio a consultar"},
                "record_type": {
                    "type": "string",
                    "description": "Tipo de registro DNS (A, AAAA, MX, NS, CNAME, TXT, PTR)",
                    "enum": ["A", "AAAA", "MX", "NS", "CNAME", "TXT", "PTR"],
                    "default": "A"
                }
            },
            "required": ["hostname"]
        }
    }
}

def run(hostname: str, record_type: str = "A") -> str:
    import dns.resolver
    import dns.exception

    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(hostname, record_type)
        results = []
        for rdata in answers:
            results.append(str(rdata))
        return f"Registros {record_type} para {hostname}:\n" + "\n".join(results)
    except ImportError:
        return "Error: La librería \"dnspython\" no está instalada. Por favor, instálala con \"pip install dnspython\"."
    except dns.resolver.NXDOMAIN:
        return f"Error: El dominio {hostname} no existe."
    except dns.resolver.NoAnswer:
        return f"Error: No se encontraron registros {record_type} para {hostname}."
    except dns.exception.DNSException as e:
        return f"Error DNS: {e}"
    except Exception as e:
        return f"Error inesperado al realizar la consulta DNS: {e}"
