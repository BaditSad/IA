from geotext import GeoText
from Answer import *
import json
import python_weather
import asyncio
import datetime
from translate import Translator
translator = Translator(to_lang="French")

def Weather(text):
    places = GeoText(text)
    if str(places.cities) != "[]" :
        city = str(places.cities)
    else :
        with open('Data\Config\Config.json', 'r', encoding='utf-8') as jsonFile :
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        for line in jsonObject["location"] :
            city = line
    asyncio.run(getweather(city, text))

async def getweather(city, text):
  async with python_weather.Client(format=python_weather.METRIC) as client:
    value = await client.get(city)
    with open('Data\Languages\FR\Options\Input_Weather.json', 'r', encoding='utf-8') as jsonFile :
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    for key in jsonObject :
        for line in jsonObject[key] :
            if line in text :
                if key == "temperature" :
                    temperature(value)
                    return
                if key == "weather_tomorrow" :
                    weather_tomorrow(value)
                    return
                if key == "weather_now" :
                    weather_now(value)
                    return

def temperature(value):
    speak("Il fait actuellement " + str(value.current.temperature) + " degrès")

def weather_now(value):
    for forecast in value.forecasts:
        if forecast.date == datetime.date.today() :
            speak(str("Actuellement, le temps est " + translator.translate(value.current.description)))

def weather_tomorrow(value):
    for forecast in value.forecasts:
        print(forecast)
        for hourly in forecast.hourly:
            print(f' --> {hourly.type!r}')
