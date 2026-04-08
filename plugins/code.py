PLUGIN_NAME = "code"
PLUGIN_DESCRIPTION = "Ejecuta código Python de forma segura en un entorno aislado (sandbox)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "code",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "python_code": {"type": "string", "description": "El código Python a ejecutar"}
            },
            "required": ["python_code"]
        }
    }
}

def run(python_code: str) -> str:
    import io
    import contextlib

    # Redirigir stdout y stderr para capturar la salida
    old_stdout = io.StringIO()
    old_stderr = io.StringIO()

    with contextlib.redirect_stdout(old_stdout), contextlib.redirect_stderr(old_stderr):
        try:
            # Ejecutar el código en un entorno limitado
            exec(python_code, {"__builtins__": {}})
            output = old_stdout.getvalue()
            errors = old_stderr.getvalue()
            if errors:
                return f"Errores de ejecución:\n{errors}\nSalida:\n{output}"
            return f"Ejecución exitosa:\n{output}"
        except Exception as e:
            return f"Error durante la ejecución del código: {e}\n{old_stderr.getvalue()}"
