PLUGIN_NAME = "currency"
PLUGIN_DESCRIPTION = "Convierte entre diferentes divisas utilizando tasas de cambio actuales."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "currency",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number", "description": "La cantidad a convertir"},
                "from_currency": {"type": "string", "description": "La divisa de origen (ej. EUR, USD)"},
                "to_currency": {"type": "string", "description": "La divisa de destino (ej. USD, GBP)"}
            },
            "required": ["amount", "from_currency", "to_currency"]
        }
    }
}

def run(amount: float, from_currency: str, to_currency: str) -> str:
    try:
        import httpx

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return f"{amount} {from_currency} es igual a {amount} {to_currency}"

        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            return f"Error: No se pudo obtener la tasa de cambio para {from_currency} a {to_currency}. Divisa no válida o no soportada."

        rate = data["rates"][to_currency]
        converted_amount = amount * rate

        return f"{amount} {from_currency} es igual a {converted_amount:.2f} {to_currency} (Tasa: {rate:.4f})"
    except httpx.RequestError as e:
        return f"Error de conexión al API de tasas de cambio: {e}"
    except ValueError:
        return "Error: La cantidad debe ser un número válido."
    except Exception as e:
        return f"Error al convertir divisa: {e}"
