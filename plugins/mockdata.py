PLUGIN_NAME = "mockdata"
PLUGIN_DESCRIPTION = "Genera datos falsos para testing (nombres, emails, direcciones, etc.)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "mockdata",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "data_type": {
                    "type": "string",
                    "description": "Tipo de dato falso a generar (name, email, address, text, date)",
                    "enum": ["name", "email", "address", "text", "date"]
                },
                "count": {
                    "type": "integer",
                    "description": "Número de elementos a generar",
                    "default": 1
                },
                "locale": {
                    "type": "string",
                    "description": "Localización para datos (ej. es_ES, en_US)",
                    "default": "en_US"
                }
            },
            "required": ["data_type"]
        }
    }
}

def run(data_type: str, count: int = 1, locale: str = "en_US") -> str:
    try:
        from faker import Faker
        fake = Faker(locale)
        results = []

        for _ in range(count):
            if data_type == "name":
                results.append(fake.name())
            elif data_type == "email":
                results.append(fake.email())
            elif data_type == "address":
                results.append(fake.address())
            elif data_type == "text":
                results.append(fake.text(max_nb_chars=50))
            elif data_type == "date":
                results.append(fake.date_this_century().isoformat())
            else:
                return "Tipo de dato falso no reconocido."
        return "\n".join(results)
    except ImportError:
        return "Error: La librería \'Faker\' no está instalada. Por favor, instálala con \'pip install Faker\'."
    except Exception as e:
        return f"Error al generar datos falsos: {e}"
