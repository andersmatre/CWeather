
import requests
import geocoder


def latlon(ip):
    # Get geographic coordinates of given IP.
    try:
        g = geocoder.ip(ip)
        return g.latlng[0], g.latlng[1]
    except TypeError:
        return None


def current_weather(api_key, lat, lon):
    # Get weather data of given geographic coordinates.
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        weather = requests.get(url).json()
    except requests.ConnectionError:
        print('Connection to api failed.')
    return weather
