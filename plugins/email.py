PLUGIN_NAME = "email"
PLUGIN_DESCRIPTION = "Envía emails simples a través de SMTP (Gmail, Outlook, etc.)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "email",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "to_address": {"type": "string", "description": "Dirección de correo electrónico del destinatario"},
                "subject": {"type": "string", "description": "Asunto del correo electrónico"},
                "body": {"type": "string", "description": "Cuerpo del mensaje del correo electrónico"},
                "from_address": {"type": "string", "description": "Dirección de correo electrónico del remitente"},
                "password": {"type": "string", "description": "Contraseña o token de aplicación del remitente (¡manejar con seguridad!)"},
                "smtp_server": {"type": "string", "description": "Servidor SMTP (ej. smtp.gmail.com)", "default": "smtp.gmail.com"},
                "smtp_port": {"type": "integer", "description": "Puerto SMTP (ej. 587 para TLS)", "default": 587}
            },
            "required": ["to_address", "subject", "body", "from_address", "password"]
        }
    }
}

def run(to_address: str, subject: str, body: str, from_address: str, password: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587) -> str:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    try:
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Habilitar seguridad TLS
            server.login(from_address, password)
            server.send_message(msg)
        return f"Email enviado exitosamente a {to_address}."
    except Exception as e:
        return f"Error al enviar el email: {e}. Asegúrate de que la dirección, contraseña y configuración SMTP sean correctas, y que las aplicaciones de terceros estén permitidas si usas Gmail/Outlook."
