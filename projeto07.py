import json
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def consultar(url):
    with urlopen(url, timeout=15) as resposta:
        return json.loads(resposta.read().decode("utf-8"))

cidade = input("Digite o nome da cidade: ").strip()

if not cidade:
    print("Digite uma cidade válida.")
    raise SystemExit

try:
    parametros = urlencode({
        "name": cidade,
        "count": 1,
        "language": "pt",
        "format": "json"
    })

    dados = consultar(
        "https://geocoding-api.open-meteo.com/v1/search?"
        + parametros
    )

    resultados = dados.get("results", [])

    if not resultados:
        print("Cidade não encontrada.")
        raise SystemExit

    local = resultados[0]
    latitude = local["latitude"]
    longitude = local["longitude"]

    parametros = urlencode({
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,"
                   "apparent_temperature,is_day,weather_code,"
                   "wind_speed_10m",
        "timezone": "auto"
    })

    clima = consultar(
        "https://api.open-meteo.com/v1/forecast?"
        + parametros
    )

    atual = clima["current"]

    codigos = {
        0: "Céu limpo",
        1: "Predominantemente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Nevoeiro",
        48: "Nevoeiro com geada",
        51: "Garoa leve",
        53: "Garoa moderada",
        55: "Garoa intensa",
        61: "Chuva leve",
        63: "Chuva moderada",
        65: "Chuva intensa",
        71: "Neve leve",
        73: "Neve moderada",
        75: "Neve intensa",
        80: "Pancadas de chuva leves",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva fortes",
        95: "Trovoadas"
    }

    print("\n=== PREVISÃO DO TEMPO ===")
    print("Cidade:", local["name"])
    print("País:", local.get("country", ""))
    print("Temperatura:", atual["temperature_2m"], "°C")
    print("Sensação térmica:", atual["apparent_temperature"], "°C")
    print("Umidade:", atual["relative_humidity_2m"], "%")
    print("Vento:", atual["wind_speed_10m"], "km/h")
    print("Condição:", codigos.get(
        atual["weather_code"], "Condição meteorológica variada"
    ))
    print("Horário da medição:", atual["time"])

except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as erro:
    print("Não foi possível consultar o clima:", erro)
