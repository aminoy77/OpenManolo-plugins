PLUGIN_NAME = "crypto"
PLUGIN_DESCRIPTION = "Obtiene el precio actual de una criptomoneda en USD."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "crypto",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "El símbolo de la criptomoneda (ej. BTC, ETH, SOL)"}
            },
            "required": ["symbol"]
        }
    }
}

def run(symbol: str) -> str:
    try:
        import httpx

        symbol = symbol.upper()
        api_url = f"https://api.coinbase.com/v2/prices/{symbol}-USD/spot"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if "data" not in data or "amount" not in data["data"]:
            return f"Error: No se pudo obtener el precio para la criptomoneda {symbol}. Símbolo no válido o no soportado."

        price = float(data["data"]["amount"])
        return f"El precio actual de {symbol} es {price:.2f} USD."
    except httpx.RequestError as e:
        return f"Error de conexión al API de Coinbase: {e}"
    except ValueError:
        return "Error: La respuesta del API no es válida."
    except Exception as e:
        return f"Error al obtener el precio de {symbol}: {e}"
