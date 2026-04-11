PLUGIN_NAME = "recipe"
PLUGIN_DESCRIPTION = "Busca recetas de cocina por nombre del plato utilizando TheMealDB API."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "recipe",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "El nombre del plato a buscar (ej. Pasta Carbonara, Chicken Curry)"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str) -> str:
    try:
        import httpx

        api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
        response = httpx.get(api_url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if not data or not data.get("meals"):
            return f"No se encontraron recetas para \'{query}\'. Intenta con otro nombre."

        recipes = data["meals"]
        output = []
        for i, recipe in enumerate(recipes[:3]): # Mostrar hasta 3 recetas
            ingredients = []
            for j in range(1, 21): # TheMealDB tiene hasta 20 ingredientes
                ingredient = recipe.get(f"strIngredient{j}")
                measure = recipe.get(f"strMeasure{j}")
                if ingredient and ingredient.strip():
                    ingredients.append(f"{ingredient.strip()} ({measure.strip()})")
            
            output.append(f"--- Receta {i+1}: {recipe.get("strMeal", "N/A")} ---")
            output.append(f"Categoría: {recipe.get("strCategory", "N/A")}")
            output.append(f"Origen: {recipe.get("strArea", "N/A")}")
            output.append(f"Ingredientes:\n  - {"\n  - ".join(ingredients)}")
            output.append(f"Instrucciones:\n{recipe.get("strInstructions", "N/A")[:500]}...") # Limitar instrucciones
            output.append(f"Ver más: {recipe.get("strYoutube", "N/A") or recipe.get("strSource", "N/A") or "N/A"}")

        return "\n\n".join(output)
    except httpx.RequestError as e:
        return f"Error de conexión al API de recetas: {e}"
    except Exception as e:
        return f"Error al buscar recetas: {e}"
