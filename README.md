# HelloChusquis-Plugins 🚀

¡Bienvenido al repositorio oficial de plugins para **HelloChusquis**! Esta es una colección de **20 plugins esenciales (Tier 1)**, refactorizados y optimizados para extender las capacidades de tu agente de terminal AI, convirtiéndolo en una herramienta de productividad ágil y robusta.

## 🛠️ Instalación

Para instalar cualquier plugin de este repositorio, simplemente ejecuta el siguiente comando en tu terminal:

```bash
hellochusquis install <nombre_del_plugin>
```

*Ejemplo: `hellochusquis install calculator`*

---

## 🧩 Plugins Disponibles (20)

| Plugin | Descripción |
| :--- | :--- |
| `calculator` | Realiza operaciones matemáticas con eval seguro. |
| `worldclock` | Hora actual en cualquier ciudad con pytz. |
| `currency` | Conversor de divisas con https://api.exchangerate-api.com/v4/latest/EUR. |
| `crypto` | Precios crypto con https://api.coinbase.com/v2/prices/{symbol}-USD/spot. |
| `ip` | Info de IP con https://ipapi.co/{ip}/json/. |
| `joke` | Chistes con https://v2.jokeapi.dev/joke/Any?lang=es. |
| `qr` | Genera QR codes con qrcode library. |
| `hash` | Genera hashes MD5/SHA256 con hashlib. |
| `base64encode` | Codifica/decodifica base64 con stdlib. |
| `password` | Genera contraseñas seguras con secrets. |
| `sysinfo` | Info del sistema con psutil. |
| `speedtest` | Test de velocidad con speedtest-cli. |
| `wikipedia` | Búsquedas Wikipedia con wikipedia library. |
| `translate` | Traducciones con deep-translator library. |
| `urlshortener` | Acorta URLs con https://tinyurl.com/api-create.php?url=. |
| `webscrape` | Extrae texto de cualquier URL con httpx + beautifulsoup4. |
| `discord` | Envía mensajes a Discord via webhook. |
| `recipe` | Busca recetas con https://www.themealdb.com/api/json/v1/1/search.php?s=. |
| `movie` | Info de películas con OMDb API. |
| `news` | Últimas noticias con https://gnews.io/api/v4/search o RSS. |

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
*Desarrollado con ❤️ por aminoy77 y la comunidad de HelloChusquis.*
