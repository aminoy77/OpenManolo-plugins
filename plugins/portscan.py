PLUGIN_NAME = "portscan"
PLUGIN_DESCRIPTION = "Escanea puertos abiertos en una dirección IP o nombre de host (con límites de seguridad)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "portscan",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Dirección IP o nombre de host a escanear"},
                "ports": {"type": "string", "description": "Puertos a escanear (ej. \"80,443,22\" o \"1-1024\")"},
                "timeout": {"type": "integer", "description": "Tiempo de espera por puerto en segundos", "default": 1}
            },
            "required": ["target", "ports"]
        }
    }
}

def run(target: str, ports: str, timeout: int = 1) -> str:
    import socket
    import re

    # Limitar el rango de puertos para evitar abusos y escaneos largos
    MAX_PORTS_TO_SCAN = 100
    MAX_PORT_NUMBER = 10000 # Evitar escanear puertos muy altos por defecto

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return f"Error: No se pudo resolver el host \'{target}\'."

    ports_to_scan = []
    if re.fullmatch(r"\d+-\d+", ports):
        start_port, end_port = map(int, ports.split("-"))
        ports_to_scan = list(range(start_port, end_port + 1))
    elif re.fullmatch(r"(\d+,)*\d+", ports):
        ports_to_scan = [int(p) for p in ports.split(",")]
    else:
        return "Error: Formato de puertos inválido. Use \"80,443\" o \"1-1024\"."

    # Aplicar límites de seguridad
    ports_to_scan = [p for p in ports_to_scan if 0 < p <= MAX_PORT_NUMBER]
    if len(ports_to_scan) > MAX_PORTS_TO_SCAN:
        return f"Error: Demasiados puertos solicitados. Límite: {MAX_PORTS_TO_SCAN}."

    open_ports = []
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(str(port))
        sock.close()

    if open_ports:
        return f"Puertos abiertos en {target} ({target_ip}): {', '.join(open_ports)}"
    else:
        return f"No se encontraron puertos abiertos en {target} ({target_ip}) en el rango especificado."
