PLUGIN_NAME = "calculator"
PLUGIN_DESCRIPTION = "Realiza operaciones matemáticas básicas de forma segura."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "La expresión matemática a evaluar (ej. \"2 + 2\")"}
            },
            "required": ["expression"]
        }
    }
}

def run(expression: str) -> str:
    try:
        # Lista blanca de operaciones y funciones permitidas
        allowed_names = {
            '__builtins__': {},
            'sqrt': lambda x: x**0.5,
            'pow': pow,
            'sin': __import__('math').sin,
            'cos': __import__('math').cos,
            'tan': __import__('math').tan,
            'log': __import__('math').log,
            'log10': __import__('math').log10,
            'pi': __import__('math').pi,
            'e': __import__('math').e,
        }
        # Evaluar la expresión de forma segura
        result = str(eval(expression, {"__builtins__": None}, allowed_names))
        return f"Resultado de '{expression}': {result}"
    except SyntaxError:
        return f"Error: Expresión matemática inválida: '{expression}'"
    except TypeError:
        return f"Error: Operación no permitida o tipo incorrecto en '{expression}'"
    except NameError as e:
        return f"Error: Función o variable no permitida en '{expression}'. {e}"
    except Exception as e:
        return f"Error al calcular '{expression}': {e}"
