PLUGIN_NAME = "fact"
PLUGIN_DESCRIPTION = "Proporciona datos curiosos o hechos aleatorios en español."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "fact",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

def run() -> str:
    import random
    facts = [
        "¿Sabías que el corazón de un colibrí late hasta 1.200 veces por minuto?",
        "¿Sabías que la Gran Muralla China no es visible desde el espacio sin ayuda óptica?",
        "¿Sabías que los pulpos tienen tres corazones?",
        "¿Sabías que el ojo de un avestruz es más grande que su cerebro?",
        "¿Sabías que la miel nunca se estropea? Se han encontrado tarros de miel comestibles en tumbas egipcias."
    ]
    return random.choice(facts)
