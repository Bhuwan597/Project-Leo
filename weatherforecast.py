from bs4 import BeautifulSoup
import requests
from speak import speak
from desktop_notify import desktop_notify
from math import floor

def weather_forecast(city):
    '''this function takes city name as argument. It scrape the google website and www.underground.com website to gather weather and temperature informations. It returns three variables search query, temperature, weather (cloudy,rainy,sunny,etc). It uses bs4 and requests module'''
    # try:
    #     search = f'Temperature in {city}'
    #     url = f'https://google.com/search?q={search}'
    #     r= requests.get(url)
    #     data = BeautifulSoup(r.text,'html.parser')
    #     temperature = data.find('div',class_='BNeawe').text
    #     url = f'https://www.wunderground.com/forecast/np/{city}'
    #     r = requests.get(url)
    #     soup = BeautifulSoup(r.text,'html.parser')
    #     weather = soup.find_all('span', class_ = 'wx-value')[1].text
    #     speak(f'Current {search} is {temperature} and weather throughout the day will be {weather}')
    #     desktop_notify('Weather Info',f'Current {search} is {temperature} and weather throughout the day will be {weather}')
    # except:
    #     speak('Sorry sir, there was an error to fetch weather related informations.')
    try:
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name 
        CITY = city
        # API key 
        API_KEY = "612c6faed68e1d51d4ca0809cc1c96ef"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            data = response.json()
            temperature = floor(data['main']['temp'] -273.15)
            weather = data['weather'][0].get('description')
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            speak(f'Current Temperature of {city} is {temperature}° C, weather is {weather}, wind speed is {wind_speed}kilometer per hour and humidity is {humidity}.')
            from time import sleep
            sleep(0.5)
            desktop_notify('Weather Report', f"Temperature: {temperature}° C\nHumidity: {humidity}\nWind Speed: {wind_speed} km/h\nWeather: {weather}")
        else:
            speak('Sorry sir, there was an error to fetch weather related informations.')
    except:
        speak('Sorry sir, there was an error to fetch weather related informations.')