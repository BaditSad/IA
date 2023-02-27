import datetime

from Answer import *

def Date():
    date = datetime.date.today()
    day = date.day
    _month = date.month
    if _month == 1 :
        month = "janvier"
    if _month == 2 :
        month = "février"
    if _month == 3 :
        month = "mars"
    if _month == 4 :
        month = "avril"
    if _month == 5 :
        month = "mai"
    if _month == 6 :
        month = "juin"
    if _month == 7 :
        month = "juillet"
    if _month == 8 :
        month = "aout"
    if _month == 9 :
        month = "septembre"
    if _month == 10 :
        month = "octobre"
    if _month == 11 :
        month = "novembre"
    if _month == 12 :
        month = "décembre"
    year = date.year
    text = "Nous sommes le {} {} {}.".format(day, month, year)
    speak(text)

def Time():
    time = datetime.datetime.now()
    if time.hour > 1:
        text = "Il est {} heures {}.".format(time.hour, time.minute)
        speak(text)
    if time.hour == 0:
        text = "Il est minuit {}.".format(time.minute)
        speak(text)
    if time.hour <= 1:
        text = "Il est {} heure {}.".format(time.hour, time.minute)
        speak(text)

