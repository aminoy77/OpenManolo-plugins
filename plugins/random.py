PLUGIN_NAME = "random"
PLUGIN_DESCRIPTION = "Genera datos aleatorios como nombres, direcciones, números, etc."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "random",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "data_type": {
                    "type": "string",
                    "description": "Tipo de dato aleatorio a generar (name, address, email, number, uuid)",
                    "enum": ["name", "address", "email", "number", "uuid"]
                },
                "locale": {
                    "type": "string",
                    "description": "Localización para datos como nombres o direcciones (ej. es_ES, en_US)",
                    "default": "en_US"
                }
            },
            "required": ["data_type"]
        }
    }
}

def run(data_type: str, locale: str = "en_US") -> str:
    try:
        from faker import Faker
        fake = Faker(locale)

        if data_type == "name":
            return fake.name()
        elif data_type == "address":
            return fake.address()
        elif data_type == "email":
            return fake.email()
        elif data_type == "number":
            return str(fake.random_int(min=1, max=100000))
        elif data_type == "uuid":
            return str(fake.uuid4())
        else:
            return "Tipo de dato aleatorio no reconocido."
    except ImportError:
        return "Error: La librería \'Faker\' no está instalada. Por favor, instálala con \'pip install Faker\'."
    except Exception as e:
        return f"Error al generar datos aleatorios: {e}"
