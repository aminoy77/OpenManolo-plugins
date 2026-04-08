PLUGIN_NAME = "quote"
PLUGIN_DESCRIPTION = "Genera citas motivacionales aleatorias en español."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "quote",
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
    quotes = [
        "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "La vida es lo que pasa mientras estás ocupado haciendo otros planes. - John Lennon",
        "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que estás haciendo, tendrás éxito. - Albert Schweitzer",
        "No te preocupes por los fracasos, preocúpate por las posibilidades que pierdes cuando ni siquiera lo intentas. - Jack Canfield",
        "Cree que puedes y ya estarás a medio camino. - Theodore Roosevelt",
        "El futuro pertenece a quienes creen en la belleza de sus sueños. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)
