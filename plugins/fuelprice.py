PLUGIN_NAME = "fuelprice"
PLUGIN_DESCRIPTION = "Obtiene los precios de la gasolina y el diésel en España por provincia o código postal."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "fuelprice",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "province": {"type": "string", "description": "Nombre de la provincia (ej. Madrid)"},
                "postal_code": {"type": "string", "description": "Código postal (ej. 28001)"},
                "fuel_type": {
                    "type": "string",
                    "description": "Tipo de combustible (gasolina95, gasolina98, diesel, diesel_plus)",
                    "enum": ["gasolina95", "gasolina98", "diesel", "diesel_plus"],
                    "default": "gasolina95"
                }
            },
            "required": []
        }
    }
}

def run(province: str = None, postal_code: str = None, fuel_type: str = "gasolina95") -> str:
    import httpx
    # En un entorno real, esto se integraría con la API del Ministerio para la Transición Ecológica y el Reto Demográfico de España.
    # La API requiere un proceso de registro y manejo de datos.
    # Para este plugin, simularemos la funcionalidad.

    if province and province.lower() == "madrid":
        if fuel_type == "gasolina95":
            return f"Precios de Gasolina 95 en Madrid (simulado): Media 1.70 EUR/litro."
        elif fuel_type == "diesel":
            return f"Precios de Diésel en Madrid (simulado): Media 1.65 EUR/litro."
        else:
            return f"Precios de {fuel_type} en Madrid (simulado): No disponible."
    elif postal_code and postal_code == "28001":
        if fuel_type == "gasolina95":
            return f"Precios de Gasolina 95 en 28001 (simulado): Media 1.72 EUR/litro."
        elif fuel_type == "diesel":
            return f"Precios de Diésel en 28001 (simulado): Media 1.68 EUR/litro."
        else:
            return f"Precios de {fuel_type} en 28001 (simulado): No disponible."
    else:
        return "No se pudo obtener el precio del combustible. Por favor, especifica una provincia o código postal válido (simulado)."
