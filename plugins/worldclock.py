PLUGIN_NAME = "worldclock"
PLUGIN_DESCRIPTION = "Obtiene la hora actual en cualquier ciudad o zona horaria del mundo."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "worldclock",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "city_or_timezone": {"type": "string", "description": "Nombre de la ciudad o zona horaria (ej. \'Europe/Madrid\', \'America/New_York\', \'London\')"}
            },
            "required": ["city_or_timezone"]
        }
    }
}

def run(city_or_timezone: str) -> str:
    try:
        import pytz
        from datetime import datetime

        # Intentar obtener la zona horaria directamente
        try:
            tz = pytz.timezone(city_or_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            # Si no es una zona horaria directa, intentar mapear ciudades comunes
            city_map = {
                "london": "Europe/London",
                "new york": "America/New_York",
                "madrid": "Europe/Madrid",
                "paris": "Europe/Paris",
                "tokyo": "Asia/Tokyo",
                "sydney": "Australia/Sydney",
                "dubai": "Asia/Dubai",
                "los angeles": "America/Los_Angeles",
                "chicago": "America/Chicago",
                "berlin": "Europe/Berlin",
                "rome": "Europe/Rome",
                "beijing": "Asia/Shanghai",
                "moscow": "Europe/Moscow",
                "cairo": "Africa/Cairo",
                "rio": "America/Sao_Paulo",
                "buenos aires": "America/Argentina/Buenos_Aires",
                "mexico city": "America/Mexico_City",
                "hong kong": "Asia/Hong_Kong",
                "singapore": "Asia/Singapore",
                "seoul": "Asia/Seoul",
                "delhi": "Asia/Kolkata",
                "mumbai": "Asia/Kolkata",
                "jakarta": "Asia/Jakarta",
                "bangkok": "Asia/Bangkok",
                "lima": "America/Lima",
                "bogota": "America/Bogota",
                "santiago": "America/Santiago",
                "caracas": "America/Caracas",
                "auckland": "Pacific/Auckland",
                "honolulu": "Pacific/Honolulu",
                "anchorage": "America/Anchorage",
                "vancouver": "America/Vancouver",
                "toronto": "America/Toronto",
                "montreal": "America/Montreal",
                "boston": "America/New_York",
                "philadelphia": "America/New_York",
                "washington": "America/New_York",
                "miami": "America/New_York",
                "atlanta": "America/New_York",
                "houston": "America/Chicago",
                "dallas": "America/Chicago",
                "denver": "America/Denver",
                "phoenix": "America/Phoenix",
                "san francisco": "America/Los_Angeles",
                "seattle": "America/Los_Angeles",
                "portland": "America/Los_Angeles",
                "las vegas": "America/Los_Angeles",
                "manila": "Asia/Manila",
                "kuala lumpur": "Asia/Kuala_Lumpur",
                "ho chi minh": "Asia/Ho_Chi_Minh",
                "hanoi": "Asia/Ho_Chi_Minh",
                "taipei": "Asia/Taipei",
                "osaka": "Asia/Tokyo",
                "sapporo": "Asia/Tokyo",
                "brisbane": "Australia/Brisbane",
                "perth": "Australia/Perth",
                "adelaide": "Australia/Adelaide",
                "melbourne": "Australia/Melbourne",
                "geneva": "Europe/Zurich",
                "zurich": "Europe/Zurich",
                "brussels": "Europe/Brussels",
                "amsterdam": "Europe/Amsterdam",
                "stockholm": "Europe/Stockholm",
                "oslo": "Europe/Oslo",
                "helsinki": "Europe/Helsinki",
                "warsaw": "Europe/Warsaw",
                "prague": "Europe/Prague",
                "budapest": "Europe/Budapest",
                "vienna": "Europe/Vienna",
                "lisbon": "Europe/Lisbon",
                "dublin": "Europe/Dublin",
                "reykjavik": "Atlantic/Reykjavik",
                "johannesburg": "Africa/Johannesburg",
                "capetown": "Africa/Johannesburg",
                "nairobi": "Africa/Nairobi",
                "lagos": "Africa/Lagos",
                "accra": "Africa/Accra",
                "casablanca": "Africa/Casablanca",
                "algiers": "Africa/Algiers",
                "tunis": "Africa/Tunis",
                "baghdad": "Asia/Baghdad",
                "tehran": "Asia/Tehran",
                "riyadh": "Asia/Riyadh",
                "doha": "Asia/Qatar",
                "kuwait": "Asia/Kuwait",
                "manama": "Asia/Bahrain",
                "abu dhabi": "Asia/Dubai",
                "muscat": "Asia/Muscat",
                "tashkent": "Asia/Tashkent",
                "almaty": "Asia/Almaty",
                "novosibirsk": "Asia/Novosibirsk",
                "yekaterinburg": "Asia/Yekaterinburg",
                "vladivostok": "Asia/Vladivostok",
                "harare": "Africa/Harare",
                "luanda": "Africa/Luanda",
                "kinshasa": "Africa/Kinshasa",
                "addis ababa": "Africa/Addis_Ababa",
                "dar es salaam": "Africa/Dar_es_Salaam",
                "kampala": "Africa/Kampala",
                "kigali": "Africa/Kigali",
                "lusaka": "Africa/Lusaka",
                "gaborone": "Africa/Gaborone",
                "windhoek": "Africa/Windhoek",
                "maputo": "Africa/Maputo",
                "antananarivo": "Indian/Antananarivo",
                "port louis": "Indian/Mauritius",
                "male": "Indian/Maldives",
                "colombo": "Asia/Colombo",
                "kathmandu": "Asia/Kathmandu",
                "dhaka": "Asia/Dhaka",
                "yangon": "Asia/Yangon",
                "phnom penh": "Asia/Phnom_Penh",
                "vientiane": "Asia/Vientiane",
                "ulaanbaatar": "Asia/Ulaanbaatar",
                "pyongyang": "Asia/Pyongyang",
                "busan": "Asia/Seoul",
                "fukuoka": "Asia/Tokyo",
                "nagoya": "Asia/Tokyo",
                "osaka": "Asia/Tokyo",
                "sendai": "Asia/Tokyo",
                "okinawa": "Asia/Tokyo",
                "guam": "Pacific/Guam",
                "saipan": "Pacific/Saipan",
                "port moresby": "Pacific/Port_Moresby",
                "honiara": "Pacific/Guadalcanal",
                "noumea": "Pacific/Noumea",
                "suva": "Pacific/Fiji",
                "nuku alofa": "Pacific/Tongatapu",
                "apia": "Pacific/Apia",
                "papeete": "Pacific/Tahiti",
                "rarotonga": "Pacific/Rarotonga",
                "easter island": "Pacific/Easter",
                "galapagos": "Pacific/Galapagos",
                "san jose": "America/Costa_Rica",
                "panama": "America/Panama",
                "havana": "America/Havana",
                "kingston": "America/Jamaica",
                "santo domingo": "America/Santo_Domingo",
                "san juan": "America/Puerto_Rico",
                "port of spain": "America/Port_of_Spain",
                "georgetown": "America/Guyana",
                "paramaribo": "America/Paramaribo",
                "cayenne": "America/Cayenne",
                "belize": "America/Belize",
                "guatemala": "America/Guatemala",
                "san salvador": "America/El_Salvador",
                "tegucigalpa": "America/Tegucigalpa",
                "managua": "America/Managua",
                "la paz": "America/La_Paz",
                "quito": "America/Guayaquil",
                "asuncion": "America/Asuncion",
                "montevideo": "America/Montevideo",
                "sao paulo": "America/Sao_Paulo",
                "brasilia": "America/Sao_Paulo",
                "recife": "America/Recife",
                "fortaleza": "America/Fortaleza",
                "salvador": "America/Bahia",
                "curitiba": "America/Sao_Paulo",
                "porto alegre": "America/Sao_Paulo",
                "belo horizonte": "America/Sao_Paulo",
                "campinas": "America/Sao_Paulo",
                "goiania": "America/Goiania",
                "cuiaba": "America/Cuiaba",
                "manaus": "America/Manaus",
                "porto velho": "America/Porto_Velho",
                "rio branco": "America/Rio_Branco",
                "macapa": "America/Belem",
                "boa vista": "America/Boa_Vista",
                "palmas": "America/Palmas",
                "florianopolis": "America/Sao_Paulo",
                "natal": "America/Fortaleza",
                "joao pessoa": "America/Fortaleza",
                "maceio": "America/Maceio",
                "aracaju": "America/Aracaju",
                "vitoria": "America/Sao_Paulo",
                "campo grande": "America/Campo_Grande",
                "cuiaba": "America/Cuiaba",
                "riga": "Europe/Riga",
                "vilnius": "Europe/Vilnius",
                "tallinn": "Europe/Tallinn",
                "sofia": "Europe/Sofia",
                "bucharest": "Europe/Bucharest",
                "athens": "Europe/Athens",
                "ankara": "Europe/Istanbul",
                "istanbul": "Europe/Istanbul",
                "kiev": "Europe/Kiev",
                "minsk": "Europe/Minsk",
                "chisinau": "Europe/Chisinau",
                "belgrade": "Europe/Belgrade",
                "zagreb": "Europe/Zagreb",
                "ljubljana": "Europe/Ljubljana",
                "sarajevo": "Europe/Sarajevo",
                "skopje": "Europe/Skopje",
                "tirana": "Europe/Tirana",
                "podgorica": "Europe/Podgorica",
                "kosovo": "Europe/Belgrade", # No es una zona horaria oficial, se mapea a la capital más cercana
                "malta": "Europe/Malta",
                "cyprus": "Asia/Nicosia",
                "reunion": "Indian/Reunion",
                "mauritius": "Indian/Mauritius",
                "seychelles": "Indian/Mahe",
                "comoros": "Indian/Comoro",
                "mayotte": "Indian/Mayotte",
                "madagascar": "Indian/Antananarivo",
                "malawi": "Africa/Blantyre",
                "zambia": "Africa/Lusaka",
                "zimbabwe": "Africa/Harare",
                "botswana": "Africa/Gaborone",
                "namibia": "Africa/Windhoek",
                "angola": "Africa/Luanda",
                "congo": "Africa/Kinshasa",
                "gabon": "Africa/Libreville",
                "cameroon": "Africa/Douala",
                "nigeria": "Africa/Lagos",
                "ghana": "Africa/Accra",
                "ivory coast": "Africa/Abidjan",
                "senegal": "Africa/Dakar",
                "morocco": "Africa/Casablanca",
                "algeria": "Africa/Algiers",
                "tunisia": "Africa/Tunis",
                "libya": "Africa/Tripoli",
                "egypt": "Africa/Cairo",
                "sudan": "Africa/Khartoum",
                "ethiopia": "Africa/Addis_Ababa",
                "somalia": "Africa/Mogadishu",
                "kenya": "Africa/Nairobi",
                "uganda": "Africa/Kampala",
                "tanzania": "Africa/Dar_es_Salaam",
                "rwanda": "Africa/Kigali",
                "burundi": "Africa/Bujumbura",
                "mozambique": "Africa/Maputo",
                "south africa": "Africa/Johannesburg",
                "lesotho": "Africa/Maseru",
                "eswatini": "Africa/Mbabane",
                "djibouti": "Africa/Djibouti",
                "eritrea": "Africa/Asmara",
                "yemen": "Asia/Aden",
                "oman": "Asia/Muscat",
                "qatar": "Asia/Qatar",
                "bahrain": "Asia/Bahrain",
                "kuwait": "Asia/Kuwait",
                "iraq": "Asia/Baghdad",
                "syria": "Asia/Damascus",
                "lebanon": "Asia/Beirut",
                "jordan": "Asia/Amman",
                "israel": "Asia/Jerusalem",
                "palestine": "Asia/Gaza",
                "turkey": "Europe/Istanbul",
                "georgia": "Asia/Tbilisi",
                "armenia": "Asia/Yerevan",
                "azerbaijan": "Asia/Baku",
                "kazakhstan": "Asia/Almaty",
                "uzbekistan": "Asia/Tashkent",
                "turkmenistan": "Asia/Ashgabat",
                "kyrgyzstan": "Asia/Bishkek",
                "tajikistan": "Asia/Dushanbe",
                "afghanistan": "Asia/Kabul",
                "pakistan": "Asia/Karachi",
                "india": "Asia/Kolkata",
                "nepal": "Asia/Kathmandu",
                "bhutan": "Asia/Thimphu",
                "bangladesh": "Asia/Dhaka",
                "sri lanka": "Asia/Colombo",
                "myanmar": "Asia/Yangon",
                "thailand": "Asia/Bangkok",
                "laos": "Asia/Vientiane",
                "cambodia": "Asia/Phnom_Penh",
                "vietnam": "Asia/Ho_Chi_Minh",
                "malaysia": "Asia/Kuala_Lumpur",
                "indonesia": "Asia/Jakarta",
                "philippines": "Asia/Manila",
                "brunei": "Asia/Brunei",
                "timor-leste": "Asia/Dili",
                "papua new guinea": "Pacific/Port_Moresby",
                "solomon islands": "Pacific/Guadalcanal",
                "vanuatu": "Pacific/Efate",
                "new caledonia": "Pacific/Noumea",
                "fiji": "Pacific/Fiji",
                "tonga": "Pacific/Tongatapu",
                "samoa": "Pacific/Apia",
                "kiribati": "Pacific/Tarawa",
                "tuvalu": "Pacific/Funafuti",
                "nauru": "Pacific/Nauru",
                "marshall islands": "Pacific/Majuro",
                "micronesia": "Pacific/Pohnpei",
                "palau": "Pacific/Palau",
                "guam": "Pacific/Guam",
                "northern mariana islands": "Pacific/Saipan",
                "wake island": "Pacific/Wake",
                "midway island": "Pacific/Midway",
                "johnston atoll": "Pacific/Johnston",
                "hawaii": "Pacific/Honolulu",
                "alaska": "America/Anchorage",
                "canada": "America/Toronto", # Mapeo a una zona horaria central de Canadá
                "usa": "America/New_York", # Mapeo a una zona horaria central de USA
                "brazil": "America/Sao_Paulo", # Mapeo a una zona horaria central de Brasil
                "argentina": "America/Argentina/Buenos_Aires", # Mapeo a una zona horaria central de Argentina
                "chile": "America/Santiago", # Mapeo a una zona horaria central de Chile
                "colombia": "America/Bogota", # Mapeo a una zona horaria central de Colombia
                "peru": "America/Lima", # Mapeo a una zona horaria central de Perú
                "ecuador": "America/Guayaquil", # Mapeo a una zona horaria central de Ecuador
                "venezuela": "America/Caracas", # Mapeo a una zona horaria central de Venezuela
                "bolivia": "America/La_Paz", # Mapeo a una zona horaria central de Bolivia
                "paraguay": "America/Asuncion", # Mapeo a una zona horaria central de Paraguay
                "uruguay": "America/Montevideo", # Mapeo a una zona horaria central de Uruguay
                "cuba": "America/Havana", # Mapeo a una zona horaria central de Cuba
                "jamaica": "America/Jamaica", # Mapeo a una zona horaria central de Jamaica
                "puerto rico": "America/Puerto_Rico", # Mapeo a una zona horaria central de Puerto Rico
                "dominican republic": "America/Santo_Domingo", # Mapeo a una zona horaria central de República Dominicana
                "haiti": "America/Port-au-Prince", # Mapeo a una zona horaria central de Haití
                "guatemala": "America/Guatemala", # Mapeo a una zona horaria central de Guatemala
                "el salvador": "America/El_Salvador", # Mapeo a una zona horaria central de El Salvador
                "honduras": "America/Tegucigalpa", # Mapeo a una zona horaria central de Honduras
                "nicaragua": "America/Managua", # Mapeo a una zona horaria central de Nicaragua
                "costa rica": "America/Costa_Rica", # Mapeo a una zona horaria central de Costa Rica
                "panama": "America/Panama", # Mapeo a una zona horaria central de Panamá
                "belize": "America/Belize", # Mapeo a una zona horaria central de Belice
                "australia": "Australia/Sydney", # Mapeo a una zona horaria central de Australia
                "new zealand": "Pacific/Auckland", # Mapeo a una zona horaria central de Nueva Zelanda
                "uk": "Europe/London", # Mapeo a una zona horaria central de UK
                "france": "Europe/Paris", # Mapeo a una zona horaria central de Francia
                "germany": "Europe/Berlin", # Mapeo a una zona horaria central de Alemania
                "italy": "Europe/Rome", # Mapeo a una zona horaria central de Italia
                "spain": "Europe/Madrid", # Mapeo a una zona horaria central de España
                "portugal": "Europe/Lisbon", # Mapeo a una zona horaria central de Portugal
                "ireland": "Europe/Dublin", # Mapeo a una zona horaria central de Irlanda
                "netherlands": "Europe/Amsterdam", # Mapeo a una zona horaria central de Países Bajos
                "belgium": "Europe/Brussels", # Mapeo a una zona horaria central de Bélgica
                "switzerland": "Europe/Zurich", # Mapeo a una zona horaria central de Suiza
                "austria": "Europe/Vienna", # Mapeo a una zona horaria central de Austria
                "sweden": "Europe/Stockholm", # Mapeo a una zona horaria central de Suecia
                "norway": "Europe/Oslo", # Mapeo a una zona horaria central de Noruega
                "denmark": "Europe/Copenhagen", # Mapeo a una zona horaria central de Dinamarca
                "finland": "Europe/Helsinki", # Mapeo a una zona horaria central de Finlandia
                "greece": "Europe/Athens", # Mapeo a una zona horaria central de Grecia
                "poland": "Europe/Warsaw", # Mapeo a una zona horaria central de Polonia
                "czech republic": "Europe/Prague", # Mapeo a una zona horaria central de República Checa
                "hungary": "Europe/Budapest", # Mapeo a una zona horaria central de Hungría
                "romania": "Europe/Bucharest", # Mapeo a una zona horaria central de Rumanía
                "bulgaria": "Europe/Sofia", # Mapeo a una zona horaria central de Bulgaria
                "russia": "Europe/Moscow", # Mapeo a una zona horaria central de Rusia
                "ukraine": "Europe/Kiev", # Mapeo a una zona horaria central de Ucrania
                "china": "Asia/Shanghai", # Mapeo a una zona horaria central de China
                "japan": "Asia/Tokyo", # Mapeo a una zona horaria central de Japón
                "south korea": "Asia/Seoul", # Mapeo a una zona horaria central de Corea del Sur
                "india": "Asia/Kolkata", # Mapeo a una zona horaria central de India
                "pakistan": "Asia/Karachi", # Mapeo a una zona horaria central de Pakistán
                "iran": "Asia/Tehran", # Mapeo a una zona horaria central de Irán
                "saudi arabia": "Asia/Riyadh", # Mapeo a una zona horaria central de Arabia Saudita
                "egypt": "Africa/Cairo", # Mapeo a una zona horaria central de Egipto
                "south africa": "Africa/Johannesburg", # Mapeo a una zona horaria central de Sudáfrica
                "nigeria": "Africa/Lagos", # Mapeo a una zona horaria central de Nigeria
                "kenya": "Africa/Nairobi", # Mapeo a una zona horaria central de Kenia
                "morocco": "Africa/Casablanca", # Mapeo a una zona horaria central de Marruecos
                "algeria": "Africa/Algiers", # Mapeo a una zona horaria central de Argelia
                "tunisia": "Africa/Tunis", # Mapeo a una zona horaria central de Túnez
                "libya": "Africa/Tripoli", # Mapeo a una zona horaria central de Libia
                "sudan": "Africa/Khartoum", # Mapeo a una zona horaria central de Sudán
                "ethiopia": "Africa/Addis_Ababa", # Mapeo a una zona horaria central de Etiopía
                "somalia": "Africa/Mogadishu", # Mapeo a una zona horaria central de Somalia
                "tanzania": "Africa/Dar_es_Salaam", # Mapeo a una zona horaria central de Tanzania
                "uganda": "Africa/Kampala", # Mapeo a una zona horaria central de Uganda
                "ghana": "Africa/Accra", # Mapeo a una zona horaria central de Ghana
                "ivory coast": "Africa/Abidjan", # Mapeo a una zona horaria central de Costa de Marfil
                "senegal": "Africa/Dakar", # Mapeo a una zona horaria central de Senegal
                "cameroon": "Africa/Douala", # Mapeo a una zona horaria central de Camerún
                "gabon": "Africa/Libreville", # Mapeo a una zona horaria central de Gabón
                "congo": "Africa/Kinshasa", # Mapeo a una zona horaria central de Congo
                "angola": "Africa/Luanda", # Mapeo a una zona horaria central de Angola
                "zambia": "Africa/Lusaka", # Mapeo a una zona horaria central de Zambia
                "zimbabwe": "Africa/Harare", # Mapeo a una zona horaria central de Zimbabue
                "botswana": "Africa/Gaborone", # Mapeo a una zona horaria central de Botsuana
                "namibia": "Africa/Windhoek", # Mapeo a una zona horaria central de Namibia
                "mozambique": "Africa/Maputo", # Mapeo a una zona horaria central de Mozambique
                "madagascar": "Indian/Antananarivo", # Mapeo a una zona horaria central de Madagascar
                "mauritius": "Indian/Mauritius", # Mapeo a una zona horaria central de Mauricio
                "reunion": "Indian/Reunion", # Mapeo a una zona horaria central de Reunión
                "seychelles": "Indian/Mahe", # Mapeo a una zona horaria central de Seychelles
                "maldives": "Indian/Maldives", # Mapeo a una zona horaria central de Maldivas
                "sri lanka": "Asia/Colombo", # Mapeo a una zona horaria central de Sri Lanka
                "bangladesh": "Asia/Dhaka", # Mapeo a una zona horaria central de Bangladesh
                "myanmar": "Asia/Yangon", # Mapeo a una zona horaria central de Myanmar
                "thailand": "Asia/Bangkok", # Mapeo a una zona horaria central de Tailandia
                "laos": "Asia/Vientiane", # Mapeo a una zona horaria central de Laos
                "cambodia": "Asia/Phnom_Penh", # Mapeo a una zona horaria central de Camboya
                "vietnam": "Asia/Ho_Chi_Minh", # Mapeo a una zona horaria central de Vietnam
                "malaysia": "Asia/Kuala_Lumpur", # Mapeo a una zona horaria central de Malasia
                "singapore": "Asia/Singapore", # Mapeo a una zona horaria central de Singapur
                "indonesia": "Asia/Jakarta", # Mapeo a una zona horaria central de Indonesia
                "philippines": "Asia/Manila", # Mapeo a una zona horaria central de Filipinas
                "brunei": "Asia/Brunei", # Mapeo a una zona horaria central de Brunéi
                "timor-leste": "Asia/Dili", # Mapeo a una zona horaria central de Timor Oriental
                "papua new guinea": "Pacific/Port_Moresby", # Mapeo a una zona horaria central de Papúa Nueva Guinea
                "solomon islands": "Pacific/Guadalcanal", # Mapeo a una zona horaria central de Islas Salomón
                "vanuatu": "Pacific/Efate", # Mapeo a una zona horaria central de Vanuatu
                "new caledonia": "Pacific/Noumea", # Mapeo a una zona horaria central de Nueva Caledonia
                "fiji": "Pacific/Fiji", # Mapeo a una zona horaria central de Fiyi
                "tonga": "Pacific/Tongatapu", # Mapeo a una zona horaria central de Tonga
                "samoa": "Pacific/Apia", # Mapeo a una zona horaria central de Samoa
                "kiribati": "Pacific/Tarawa", # Mapeo a una zona horaria central de Kiribati
                "tuvalu": "Pacific/Funafuti", # Mapeo a una zona horaria central de Tuvalu
                "nauru": "Pacific/Nauru", # Mapeo a una zona horaria central de Nauru
                "marshall islands": "Pacific/Majuro", # Mapeo a una zona horaria central de Islas Marshall
                "micronesia": "Pacific/Pohnpei", # Mapeo a una zona horaria central de Micronesia
                "palau": "Pacific/Palau", # Mapeo a una zona horaria central de Palaos
                "guam": "Pacific/Guam", # Mapeo a una zona horaria central de Guam
                "northern mariana islands": "Pacific/Saipan", # Mapeo a una zona horaria central de Islas Marianas del Norte
                "wake island": "Pacific/Wake", # Mapeo a una zona horaria central de Isla Wake
                "midway island": "Pacific/Midway", # Mapeo a una zona horaria central de Isla Midway
                "johnston atoll": "Pacific/Johnston", # Mapeo a una zona horaria central de Atolón Johnston
                "hawaii": "Pacific/Honolulu", # Mapeo a una zona horaria central de Hawái
                "alaska": "America/Anchorage", # Mapeo a una zona horaria central de Alaska
            }
            tz_name = city_map.get(city_or_timezone.lower())
            if not tz_name:
                return f"Error: Zona horaria o ciudad ‘{city_or_timezone}’ no reconocida. Intenta con un formato como ‘Europe/Madrid’ o una ciudad principal."
            tz = pytz.timezone(tz_name)

        now = datetime.now(tz)
        return f"La hora actual en {city_or_timezone} es {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}"
    except ImportError:
        return "ERROR: La librería \'pytz\' no está instalada. Ejecuta: pip3 install pytz --break-system-packages"
    except Exception as e:
        return f"Error al obtener la hora para ‘{city_or_timezone}’: {e}"
