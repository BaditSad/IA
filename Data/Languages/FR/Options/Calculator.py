import json
import re

from Answer import *

def Calculator(text):
    with open('Data\Languages\FR\Options\Input_Calculator.json', 'r', encoding='utf-8') as jsonFile :
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    for key in jsonObject :
        for line in jsonObject[key] :
            if line in text :
                key1 = key
                num = re.findall(r'\d*\.?\d+', text)
                if key1 == "addition" : 
                    if check(text, key1) == True:
                        speak("Je ne suis pas programmé pour répondre à cette demande.")
                        return
                    else :
                        speak(Addition(num))
                        return
                if key1 == "soustraction" : 
                    if check(text, key1) == True:
                        speak("Je ne suis pas programmé pour répondre à cette demande.")
                        return
                    else :
                        speak(Addition(num))
                        return
                if key1 == "multiplication" : 
                    if check(text, key1) == True:
                        speak("Je ne suis pas programmé pour répondre à cette demande.")
                        return
                    else :
                        speak(Addition(num))
                        return
                if key1 == "division" : 
                    if check(text, key1) == True:
                        speak("Je ne suis pas programmé pour répondre à cette demande.")
                        return
                    else :
                        speak(Addition(num))
                        return
                if key1 == "modulo" : 
                    if check(text, key1) == True:
                        speak("Je ne suis pas programmé pour répondre à cette demande.")
                        return
                    else :
                        speak(Addition(num))
                        return

def check(text, key1):
    ok = False
    with open('Data\Languages\FR\Options\Input_Calculator.json', 'r', encoding='utf-8') as jsonFile :
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    for key2 in jsonObject :
        for line in jsonObject[key2] :
            if line in text :
                if key1 != key2 :
                    ok = True
    return ok
                
def Addition(num):
    value = int(num[0])
    num.pop(0)
    for x in num :
        value += int(x)
    return value

def Soustraction(num):
    value = int(num[0])
    num.pop(0)
    for x in num :
        value -= int(x)
    return value

def Multiplication(num):
    value = int(num[0])
    num.pop(0)
    for x in num :
        value *= int(x)
    return value

def Division(num):
    value = int(num[0])
    num.pop(0)
    for x in num :
        value /= int(x)
    return value

def Modulo(num):
    value = int(num[0])
    num.pop(0)
    for x in num :
        value %= int(x)
    return value