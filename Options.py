from Answer import *
from Data.Languages.FR.Options.Date import *
from Data.Languages.FR.Options.Calculator import *
from Data.Languages.FR.Options.Weather import *

def Options_choice(option, text):
    if option == "stop" :
        exit()
    if option == "calculator" :
        Calculator(text)
    if option == "date" :
        Date()
    if option == "time" :
        Time()
    if option == "weather" :
        Weather(text)