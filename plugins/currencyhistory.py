PLUGIN_NAME = "currencyhistory"
PLUGIN_DESCRIPTION = "Obtiene el historial de tipos de cambio entre dos monedas para un rango de fechas."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "currencyhistory",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "base_currency": {"type": "string", "description": "Código ISO de la moneda base (ej. EUR)"},
                "target_currency": {"type": "string", "description": "Código ISO de la moneda objetivo (ej. USD)"},
                "start_date": {"type": "string", "description": "Fecha de inicio en formato YYYY-MM-DD"},
                "end_date": {"type": "string", "description": "Fecha de fin en formato YYYY-MM-DD"}
            },
            "required": ["base_currency", "target_currency", "start_date", "end_date"]
        }
    }
}

def run(base_currency: str, target_currency: str, start_date: str, end_date: str) -> str:
    import httpx
    import datetime

    try:
        # Usaremos la API de ExchangeRate-API como ejemplo. Requiere una clave API gratuita.
        # Para este ejemplo, simularemos la respuesta.
        # API_KEY = "TU_API_KEY_DE_EXCHANGERATE_API"
        # url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/history/{base_currency}/{start_date}"

        start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        if start_dt > end_dt:
            return "Error: La fecha de inicio no puede ser posterior a la fecha de fin."

        # Simulación de datos históricos
        if base_currency.upper() == "EUR" and target_currency.upper() == "USD":
            output = f"Historial de tipos de cambio EUR a USD entre {start_date} y {end_date} (simulado):\n"
            current_date = start_dt
            while current_date <= end_dt:
                # Variación simulada
                rate = 1.08 + (current_date.day % 10) * 0.002
                output += f"  {current_date.strftime("%Y-%m-%d")}: 1 EUR = {rate:.4f} USD\n"
                current_date += datetime.timedelta(days=1)
            return output
        else:
            return f"Historial de tipos de cambio para {base_currency} a {target_currency} no disponible en la simulación."

    except ValueError:
        return "Error: Formato de fecha inválido. Use YYYY-MM-DD."
    except Exception as e:
        return f"Error inesperado al obtener el historial de tipos de cambio: {e}"
