PLUGIN_NAME = "goldprice"
PLUGIN_DESCRIPTION = "Obtiene el precio actual del oro, plata y otros metales preciosos."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "goldprice",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "metal": {
                    "type": "string",
                    "description": "Metal precioso (gold, silver, platinum)",
                    "enum": ["gold", "silver", "platinum"],
                    "default": "gold"
                },
                "currency": {
                    "type": "string",
                    "description": "Moneda para el precio (USD, EUR)",
                    "enum": ["USD", "EUR"],
                    "default": "USD"
                }
            },
            "required": []
        }
    }
}

def run(metal: str = "gold", currency: str = "USD") -> str:
    import httpx
    try:
        # Usaremos una API gratuita o simularemos los datos.
        # Para datos en tiempo real, se necesitaría una API como Gold Price API o similar.
        # Simulación de precios
        prices = {
            "gold": {"USD": 2300.00, "EUR": 2150.00},
            "silver": {"USD": 28.00, "EUR": 26.00},
            "platinum": {"USD": 980.00, "EUR": 910.00}
        }
        
        if metal.lower() in prices and currency.upper() in prices[metal.lower()]:
            price = prices[metal.lower()][currency.upper()]
            return f"Precio actual de {metal.capitalize()} en {currency.upper()}: {price:.2f}"
        else:
            return f"No se encontró el precio para {metal.capitalize()} en {currency.upper()} (simulado)."

    except Exception as e:
        return f"Error al obtener el precio del metal: {e}"
