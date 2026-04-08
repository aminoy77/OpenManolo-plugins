PLUGIN_NAME = "pomodoro"
PLUGIN_DESCRIPTION = "Inicia un temporizador Pomodoro para sesiones de trabajo y descanso."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pomodoro",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "duration": {"type": "integer", "description": "Duración de la sesión de trabajo en minutos (por defecto 25)", "default": 25},
                "break_duration": {"type": "integer", "description": "Duración del descanso en minutos (por defecto 5)", "default": 5}
            },
            "required": []
        }
    }
}

def run(duration: int = 25, break_duration: int = 5) -> str:
    # En un entorno real, esto iniciaría un temporizador en segundo plano
    # y notificaría al usuario cuando termine cada fase.
    return f"Temporizador Pomodoro iniciado: {duration} minutos de trabajo, {break_duration} minutos de descanso. (Simulado)"
