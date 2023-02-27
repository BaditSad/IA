import json
import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

def speak(text):
        print(text)
        engine.say(text)
        engine.runAndWait()

def Answer(file, file_category):
    with open(file, 'r', encoding='utf-8') as jsonFile :
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    speak(random.choice(jsonObject[file_category]))