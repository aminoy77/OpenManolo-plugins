PLUGIN_NAME = "lottery"
PLUGIN_DESCRIPTION = "Genera números aleatorios para diferentes tipos de lotería (Primitiva, Bonoloto, Euromillones)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "lottery",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "game": {
                    "type": "string",
                    "description": "Tipo de lotería (primitiva, bonoloto, euromillones)",
                    "enum": ["primitiva", "bonoloto", "euromillones"]
                }
            },
            "required": ["game"]
        }
    }
}

def run(game: str) -> str:
    import random

    if game == "primitiva":
        numbers = sorted(random.sample(range(1, 50), 6))
        complementary = random.choice([n for n in range(1, 50) if n not in numbers])
        reimbursement = random.randint(0, 9)
        return f"Primitiva: Números: {numbers}, Complementario: {complementary}, Reintegro: {reimbursement}"
    elif game == "bonoloto":
        numbers = sorted(random.sample(range(1, 50), 6))
        complementary = random.choice([n for n in range(1, 50) if n not in numbers])
        reimbursement = random.randint(0, 9)
        return f"Bonoloto: Números: {numbers}, Complementario: {complementary}, Reintegro: {reimbursement}"
    elif game == "euromillones":
        main_numbers = sorted(random.sample(range(1, 51), 5))
        stars = sorted(random.sample(range(1, 13), 2))
        return f"Euromillones: Números principales: {main_numbers}, Estrellas: {stars}"
    else:
        return "Juego de lotería no reconocido. Opciones: primitiva, bonoloto, euromillones."
