PLUGIN_NAME = "timer"
PLUGIN_DESCRIPTION = "Inicia un temporizador con alarma y notificación."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "timer",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "duration_seconds": {"type": "integer", "description": "Duración del temporizador en segundos"},
                "message": {"type": "string", "description": "Mensaje de la alarma cuando el temporizador termine"}
            },
            "required": ["duration_seconds", "message"]
        }
    }
}

def run(duration_seconds: int, message: str) -> str:
    import time
    # En un entorno real, esto se ejecutaría en un hilo separado o un proceso en segundo plano
    # para no bloquear el agente principal y emitir una notificación real.
    if duration_seconds <= 0:
        return "Error: La duración del temporizador debe ser un valor positivo."
    
    # Simulación de espera
    # time.sleep(duration_seconds) # Descomentar para una espera real (bloqueante)
    
    return f"Temporizador iniciado por {duration_seconds} segundos. Alarma: \"{message}\". (Simulado)"
