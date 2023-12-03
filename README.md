## Opis projektu
Projekt ten zawiera skrypt napisany w języku Python, który umożliwia pobieranie informacji dotyczących prognozy pogody w obecnym dniu z serwisu internetowego [weather.virtualcrossing.com ](https://weather.visualcrossing.com) za pomocą udostępnionego API.

## Technologie
- **Python:** Skrypt został napisany w języku Python, wykorzystując jego biblioteki do komunikacji z interfejsem API oraz przetwarzania danych.
- **Biblioteki zewnętrzne:** Projekt wykorzystuje biblioteki `requests` do wysyłania zapytań do API oraz `Flask` z `jsonify` do stworzenia aplikacji webowej i generowania odpowiedzi HTTP w formacie JSON.

## Instrukcja instalacji
1. Stworzenie wirtualnego środowiska
```
mkdir weatherAPI &&
cd weatherAPI &&
python3 -m venv venvWeatherAPI
```

2. Aktywacja wirtualnego środowiska
```
source venvWeatherAPI/bin/activate
```

3. Klonowanie repozytorium
```
git clone https://github.com/wojtekbakun/WeatherAPI.git
```

4. Instalacja dodatkowych pakietów:
```
pip install -r requirements.txt
```

-  *po skończonej pracy w środowisku wirtualnym należy je dezaktywować za pomocą komendy:* 
```
deactivate
```
## Przewodnik użytkowania
W terminalu należy wpisać następującą komendę:
```
python3 weather_app.py
```

W odpowiedzi powinien pokazać się następujący komunikat:
```
Serving Flask app 'weather_app'
Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://127.0.0.1:5000
Press CTRL+C to quit
Restarting with stat
Debugger is active!
Debugger PIN: 441-955-257
```

Teraz wpisz w przeglądarce adres z tej linijki:
```
Running on http://127.0.0.1:5000
```

W przeglądarce możesz wpisać następujące endpointy:
- `/get-weather` - cały plik json odebrany od dostawcy API dla miasta Warszawa
- `/get-wather/city` po wpisaniu miasta w języku angielskim w miejsce `<city>` pokaże się odczuwalna temperatura dla wybranego miasta w obecnej chwili
## Przykłady korzystania
Oto okna, które pokażą się w zależności od zastosowanych endpointów:

- brak endpointu
![Screenshot 2023-12-03 at 18 31 34](https://github.com/wojtekbakun/WeatherAPI/assets/129949845/335c387b-7c2a-4dfb-b4e7-92d40503acda)

- `/get-weather` (fragment json)
![Screenshot 2023-12-03 at 18 40 21](https://github.com/wojtekbakun/WeatherAPI/assets/129949845/29d8752b-2931-400f-9d3f-80f74ae6e0b2)

- `/get-weather/<szczecin>`
![Screenshot 2023-12-03 at 18 41 02](https://github.com/wojtekbakun/WeatherAPI/assets/129949845/80344018-3381-46b7-8f4f-351c45ff75d8)
