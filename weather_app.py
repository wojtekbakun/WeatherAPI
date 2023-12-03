import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# Funkcja do pobierania danych pogodowych z API
def fetch_weather_data(city):
    api_key = "WA825WJEGFTB4YS6PLJNSMNHU"
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}&contentType=json"

    try:
        # Wysłanie zapytania GET do API
        response = requests.get(base_url)
        response.raise_for_status()  # Sprawdzenie, czy odpowiedź zwraca kod sukcesu (status kodu 2xx)

        # Pobranie danych pogodowych w formacie JSON z odpowiedzi API
        weather_data = response.json()
        return weather_data

    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.RequestException as e:
        print(f"Request error occurred: {e}")

# Endpoint w Flasku do zwracania danych pogodowych
@app.route("/get-weather")
def get_weather():
    # Wywołanie funkcji fetch_weather_data() do pobrania danych pogodowych
    weather_data = fetch_weather_data("warsaw")
    
    # Sprawdzenie, czy dane pogodowe zostały pobrane prawidłowo
    if weather_data:
        # Zwrócenie danych pogodowych w formacie JSON z kodem statusu HTTP 200 (sukces)
        return jsonify({"data": weather_data}), 200
    else:
        # Zwrócenie komunikatu o błędzie w przypadku niepowodzenia pobrania danych z kodem statusu HTTP 500 (błąd serwera)
        return jsonify({"error": "Failed to fetch weather data"}), 500
    
@app.route(f"/get-weather/<city>")
def get_weather_for_city(city):
     # Wywołanie funkcji fetch_weather_data() do pobrania danych pogodowych
    weather_data = fetch_weather_data(f"{city}")

    weather_data_cleared = weather_data["currentConditions"]["feelslike"]
    # Sprawdzenie, czy dane pogodowe zostały pobrane prawidłowo
    if weather_data:
        # Zwrócenie danych pogodowych w formacie JSON z kodem statusu HTTP 200 (sukces)
        #return jsonify({"data": weather_data}), 200
        return jsonify({"odczuwalna temperatura": weather_data_cleared}), 201
    else:
        # Zwrócenie komunikatu o błędzie w przypadku niepowodzenia pobrania danych z kodem statusu HTTP 500 (błąd serwera)
        return jsonify({"error": "Failed to fetch weather data"}), 500
    

# Główna część programu - uruchomienie aplikacji Flask
if __name__ == "__main__":
    app.run(debug=True)
