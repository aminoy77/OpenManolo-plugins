# HelloChusquis-Plugins 🚀

¡Bienvenido al repositorio oficial de plugins para **HelloChusquis**! Esta es una colección masiva de **81 plugins** diseñados para extender las capacidades de tu agente de terminal AI, convirtiéndolo en una herramienta de productividad definitiva.

## 🛠️ Instalación

Para instalar cualquier plugin de este repositorio, simplemente ejecuta el siguiente comando en tu terminal:

```bash
hellochusquis install <nombre_del_plugin>
```

*Ejemplo: `hellochusquis install weather`*

---

## 🧩 Plugins Disponibles (81)

| Categoría | Plugin | Descripción |
| :--- | :--- | :--- |
| **Utilidades** | `calculator` | Operaciones aritméticas básicas. |
| | `unit` | Conversor de unidades (peso, longitud, temp, etc.). |
| | `password` | Generador de contraseñas seguras. |
| | `qr` | Generador de códigos QR. |
| | `urlshortener` | Acortador de enlaces (TinyURL). |
| | `ascii` | Generador de arte ASCII. |
| | `pdf` | Crea un archivo PDF real con título y secciones de contenido. |
| | `docx` | Crea un archivo Microsoft Word .docx real con título y secciones de contenido. |
| | `base64` | Codifica y decodifica texto o archivos en Base64. |
| | `hash` | Genera hashes criptográficos (MD5, SHA256, etc.). |
| | `compress` | Comprime y descomprime archivos o directorios. |
| | `backup` | Crea copias de seguridad de directorios. |
| | `diff` | Compara diferencias entre archivos o textos. |
| | `barcode` | Genera y lee códigos de barras. |
| | `color` | Convierte colores entre formatos (hex, rgb, hsl, nombre). |
| **Información** | `wikipedia` | Búsquedas rápidas en Wikipedia. |
| | `definition` | Diccionario de definiciones en español. |
| | `dictionary` | Diccionario avanzado (sinónimos, antónimos). |
| | `weather` | Clima actual y pronóstico por ciudad. |
| | `news` | Últimas noticias por tema o categoría. |
| | `ip` | Información de IP pública y geolocalización. |
| | `whois` | Información WHOIS de dominios. |
| | `worldclock` | Hora actual en cualquier ciudad del mundo. |
| | `rss` | Lee feeds RSS y noticias por temática. |
| | `webscrape` | Extrae información específica de cualquier página web. |
| | `sslcheck` | Verifica certificado SSL de un dominio. |
| **Productividad** | `todo` | Lista de tareas persistente. |
| | `calendar` | Gestión de eventos y recordatorios. |
| | `reminder` | Sistema de recordatorios con fecha/hora. |
| | `pomodoro` | Temporizador de trabajo/descanso. |
| | `expense` | Control de gastos personales. |
| | `habit` | Tracker de hábitos diarios. |
| | `timer` | Temporizador con alarma y notificación. |
| | `alarm` | Programa alarmas con mensaje y hora. |
| | `meeting` | Crea enlaces de Zoom, Google Meet o Teams (simulado). |
| **Comunicación** | `email` | Envía emails simples (SMTP). |
| | `linkedin` | Busca perfiles o jobs en LinkedIn (simulado). |
| | `twitter` | Busca tweets o trending topics (simulado). |
| | `reddit` | Busca posts y comentarios en Reddit (simulado). |
| | `instagram` | Info básica de perfiles públicos (simulado). |
| | `tiktok` | Busca vídeos trending o por hashtag (simulado). |
| | `discord` | Envía mensajes a canales de Discord (webhook). |
| | `telegram` | Envía mensajes o notificaciones vía Telegram. |
| | `whatsapp` | Envía mensajes vía WhatsApp Web (simulado). |
| **Desarrollo** | `git` | Asistente para comandos Git. |
| | `filemanager` | Gestión de archivos y directorios. |
| | `shell` | Ejecución segura de comandos del sistema. |
| | `code` | Ejecutor de código Python (Sandbox). |
| | `ping` | Comprobación de conectividad de red. |
| | `speedtest` | Test de velocidad de internet. |
| | `sysinfo` | Información del sistema y hardware. |
| | `battery` | Estado detallado de la batería. |
| | `regex` | Tester y explicador de expresiones regulares. |
| | `portscan` | Escanea puertos abiertos de una IP (con límites). |
| | `dnslookup` | Consultas DNS (IP, MX, NS, etc.). |
| **Multimedia** | `spotify` | Control de reproducción y búsquedas. |
| | `youtube` | Búsqueda e info de videos. |
| | `imagegen` | Generador de prompts para IAs de imagen. |
| | `meme` | Generador de memes de texto. |
| | `emoji` | Buscador y generador de emojis. |
| | `voice` | Convierte texto a voz y reproduce (simulado). |
| | `speech` | Reconocimiento de voz a texto (simulado). |
| **Finanzas** | `crypto` | Precios de criptomonedas en tiempo real. |
| | `stocks` | Precios de acciones y bolsa. |
| | `currency` | Conversor de divisas con tasas actuales. |
| | `currencyhistory` | Historial de tipos de cambio. |
| | `goldprice` | Precio del oro, plata y otros metales. |
| | `fuelprice` | Precios de gasolina y diésel en España. |
| **Estilo de Vida** | `recipe` | Buscador de recetas de cocina. |
| | `movie` | Info de películas y series (OMDb). |
| | `horoscope` | Horóscopo diario por signo. |
| | `maps` | Direcciones y distancias entre ciudades. |
| | `flight` | Estado e info de vuelos. |
| | `train` | Horarios de trenes (Renfe, AVE, etc.). |
| | `bus` | Horarios de autobuses y metros en ciudades españolas. |
| **Diversión** | `joke` | Chistes aleatorios en español. |
| | `fact` | Datos curiosos y hechos aleatorios. |
| | `quote` | Citas motivacionales aleatorias. |
| | `lottery` | Generador de números de lotería. |
| | `age` | Calculadora de edad exacta. |
| | `bmi` | Calculadora de Índice de Masa Corporal. |
| | `random` | Generador de datos aleatorios (personas, direcciones, etc.). |
| | `mockdata` | Genera datos falsos para testing. |
| | `translatefile` | Traduce archivos de texto completos. |

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
