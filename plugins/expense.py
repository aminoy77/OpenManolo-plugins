PLUGIN_NAME = "expense"
PLUGIN_DESCRIPTION = "Registra y gestiona gastos personales de forma persistente."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "expense",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (add, list, total)",
                    "enum": ["add", "list", "total"]
                },
                "amount": {
                    "type": "number",
                    "description": "Cantidad del gasto (requerido para add)"
                },
                "category": {
                    "type": "string",
                    "description": "Categoría del gasto (ej. comida, transporte, ocio) (requerido para add)"
                },
                "description": {
                    "type": "string",
                    "description": "Descripción opcional del gasto"
                }
            },
            "required": ["action"]
        }
    }
}

# Simulación de almacenamiento de gastos
expenses = []

def run(action: str, amount: float = None, category: str = None, description: str = None) -> str:
    import datetime

    if action == "add":
        if amount is None or category is None:
            return "Error: Cantidad y categoría son requeridos para añadir un gasto."
        expenses.append({"date": datetime.date.today().isoformat(), "amount": amount, "category": category, "description": description})
        return f"Gasto de {amount} en {category} registrado."
    elif action == "list":
        if not expenses:
            return "No hay gastos registrados."
        output = "Lista de Gastos:\n"
        for exp in expenses:
            output += f"Fecha: {exp["date"]}, Cantidad: {exp["amount"]}, Categoría: {exp["category"]}, Descripción: {exp["description"] or "N/A"}\n"
        return output
    elif action == "total":
        total_amount = sum(exp["amount"] for exp in expenses)
        return f"Total de gastos registrados: {total_amount}"
    else:
        return "Acción de gastos no reconocida."
