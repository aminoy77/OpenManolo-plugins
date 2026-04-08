PLUGIN_NAME = "horoscope"
PLUGIN_DESCRIPTION = "Obtiene el horóscopo diario para un signo zodiacal específico."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "horoscope",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "Signo zodiacal (ej. Aries, Tauro, Géminis)",
                    "enum": [
                        "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
                        "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"
                    ]
                }
            },
            "required": ["sign"]
        }
    }
}

def run(sign: str) -> str:
    import httpx
    try:
        # Para un uso real, se integraría con una API de horóscopos.
        # Aquí se simula una respuesta.
        horoscopes = {
            "Aries": "Hoy es un buen día para tomar iniciativas y liderar proyectos. Tu energía está en su punto máximo.",
            "Tauro": "Enfócate en tus finanzas y en la estabilidad. Es un buen momento para planificar a largo plazo.",
            "Géminis": "La comunicación será clave hoy. Expresa tus ideas claramente y escucha a los demás.",
            "Cáncer": "Dedica tiempo a tu hogar y familia. Busca la comodidad y el bienestar emocional.",
            "Leo": "Tu creatividad y carisma están en alza. Aprovecha para brillar en tus actividades.",
            "Virgo": "Organiza tus tareas y cuida tu salud. La eficiencia será tu mejor aliada.",
            "Libra": "Busca el equilibrio en tus relaciones personales y profesionales. La armonía es fundamental.",
            "Escorpio": "Es un día para la introspección y la transformación. Confía en tu intuición.",
            "Sagitario": "Aventúrate en nuevas experiencias y conocimientos. Tu espíritu explorador te guiará.",
            "Capricornio": "Concéntrate en tus metas profesionales. La disciplina y el esfuerzo darán sus frutos.",
            "Acuario": "Conecta con tus amigos y la comunidad. Las ideas innovadoras surgirán de la colaboración.",
            "Piscis": "Escucha tu voz interior y dedica tiempo a la espiritualidad. La empatía te conectará con los demás."
        }
        return horoscopes.get(sign, f"Horóscopo no disponible para el signo {sign}.")
    except Exception as e:
        return f"Error al obtener el horóscopo: {e}"
