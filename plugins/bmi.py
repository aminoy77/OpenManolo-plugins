PLUGIN_NAME = "bmi"
PLUGIN_DESCRIPTION = "Calcula el Índice de Masa Corporal (IMC) y proporciona una clasificación."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "bmi",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "weight_kg": {"type": "number", "description": "Peso en kilogramos"},
                "height_m": {"type": "number", "description": "Altura en metros"}
            },
            "required": ["weight_kg", "height_m"]
        }
    }
}

def run(weight_kg: float, height_m: float) -> str:
    if height_m <= 0:
        return "Error: La altura debe ser un valor positivo."
    if weight_kg <= 0:
        return "Error: El peso debe ser un valor positivo."

    bmi = weight_kg / (height_m ** 2)
    classification = ""
    if bmi < 18.5:
        classification = "Bajo peso"
    elif 18.5 <= bmi < 24.9:
        classification = "Peso normal"
    elif 25 <= bmi < 29.9:
        classification = "Sobrepeso"
    else:
        classification = "Obesidad"

    return f"Tu IMC es: {bmi:.2f} ({classification})"
