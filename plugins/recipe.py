PLUGIN_NAME = "recipe"
PLUGIN_DESCRIPTION = "Busca recetas de cocina por ingredientes o nombre del plato."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "recipe",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Ingredientes o nombre del plato a buscar"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str) -> str:
    # En un entorno real, esto se integraría con una API de recetas (ej. Spoonacular, Edamam).
    # Aquí se simula la funcionalidad.
    if "pasta" in query.lower():
        return "Receta de Pasta Carbonara: Ingredientes: pasta, huevos, panceta, queso parmesano. Pasos: Cocer pasta, freír panceta, mezclar con huevos y queso." 
    elif "pollo" in query.lower():
        return "Receta de Pollo al Ajillo: Ingredientes: pollo, ajos, vino blanco, perejil. Pasos: Dorar pollo, añadir ajos, vino y perejil, cocinar a fuego lento."
    else:
        return f"Buscando recetas para \'{query}\'. No se encontraron resultados específicos. (Simulado)"
