# HelloChusquis-Plugins 🚀

¡Bienvenido al repositorio oficial de plugins para **HelloChusquis**! Esta es una colección masiva de **45 plugins** diseñados para extender las capacidades de tu agente de terminal AI, convirtiéndolo en una herramienta de productividad definitiva.

## 🛠️ Instalación

Para instalar cualquier plugin de este repositorio, simplemente ejecuta el siguiente comando en tu terminal:

```bash
hellochusquis install <nombre_del_plugin>
```

*Ejemplo: `hellochusquis install weather`*

---

## 🧩 Plugins Disponibles (45)

| Categoría | Plugin | Descripción |
| :--- | :--- | :--- |
| **Utilidades** | `calculator` | Operaciones aritméticas básicas. |
| | `unit` | Conversor de unidades (peso, longitud, temp, etc.). |
| | `password` | Generador de contraseñas seguras. |
| | `qr` | Generador de códigos QR. |
| | `urlshortener` | Acortador de enlaces (TinyURL). |
| | `ascii` | Generador de arte ASCII. |
| | `pdf` | Extractor de texto de archivos PDF. |
| **Información** | `wikipedia` | Búsquedas rápidas en Wikipedia. |
| | `definition` | Diccionario de definiciones en español. |
| | `dictionary` | Diccionario avanzado (sinónimos, antónimos). |
| | `weather` | Clima actual y pronóstico por ciudad. |
| | `news` | Últimas noticias por tema o categoría. |
| | `ip` | Información de IP pública y geolocalización. |
| | `whois` | Información WHOIS de dominios. |
| | `worldclock` | Hora actual en cualquier ciudad del mundo. |
| **Productividad** | `todo` | Lista de tareas persistente. |
| | `calendar` | Gestión de eventos y recordatorios. |
| | `reminder` | Sistema de recordatorios con fecha/hora. |
| | `pomodoro` | Temporizador de trabajo/descanso. |
| | `expense` | Control de gastos personales. |
| | `habit` | Tracker de hábitos diarios. |
| **Desarrollo** | `git` | Asistente para comandos Git. |
| | `filemanager` | Gestión de archivos y directorios. |
| | `shell` | Ejecución segura de comandos del sistema. |
| | `code` | Ejecutor de código Python (Sandbox). |
| | `ping` | Comprobación de conectividad de red. |
| | `speedtest` | Test de velocidad de internet. |
| | `sysinfo` | Información del sistema y hardware. |
| | `battery` | Estado detallado de la batería. |
| **Multimedia** | `spotify` | Control de reproducción y búsquedas. |
| | `youtube` | Búsqueda e info de videos. |
| | `imagegen` | Generador de prompts para IAs de imagen. |
| | `meme` | Generador de memes de texto. |
| | `emoji` | Buscador y generador de emojis. |
| **Finanzas** | `crypto` | Precios de criptomonedas en tiempo real. |
| | `stocks` | Precios de acciones y bolsa. |
| | `currency` | Conversor de divisas con tasas actuales. |
| **Estilo de Vida** | `recipe` | Buscador de recetas de cocina. |
| | `movie` | Info de películas y series (OMDb). |
| | `horoscope` | Horóscopo diario por signo. |
| | `maps` | Direcciones y distancias entre ciudades. |
| | `flight` | Estado e info de vuelos. |
| **Diversión** | `joke` | Chistes aleatorios en español. |
| | `fact` | Datos curiosos y hechos aleatorios. |
| | `quote` | Citas motivacionales aleatorias. |
| | `lottery` | Generador de números de lotería. |
| | `age` | Calculadora de edad exacta. |
| | `bmi` | Calculadora de Índice de Masa Corporal. |

---

## ✍️ Creación de Plugins

Si deseas contribuir con un nuevo plugin, sigue esta estructura oficial:

```python
PLUGIN_NAME = "mi_plugin"
PLUGIN_DESCRIPTION = "Descripción útil en español"
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "mi_plugin",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "param": {"type": "string", "description": "Descripción del parámetro"}
            },
            "required": ["param"]
        }
    }
}

def run(param: str) -> str:
    try:
        # Tu lógica aquí
        return f"Resultado: {param}"
    except Exception as e:
        return f"Error: {e}"
```

---

## 🤝 Contribuir

1. Haz un **Fork** del proyecto.
2. Crea una rama para tu mejora: `git checkout -b feature/nuevo-plugin`.
3. Haz un **Commit** de tus cambios: `git commit -m 'Añadir plugin X'`.
4. Sube los cambios: `git push origin feature/nuevo-plugin`.
5. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
*Desarrollado con ❤️ por Arnau y la comunidad de HelloChusquis.*
