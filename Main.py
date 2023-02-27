import speech_recognition as sr
from Analyze import *
from Answer import *

DEBUG = True

recognizer = sr.Recognizer()
microphone = sr.Microphone()

class IA:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def hear(self, recognizer, microphone):
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio, language='fr-FR')
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")

    def analyze(self, command):
        try:
            Analyze_text(command)
        except TypeError:
            print("Warning: You're getting a TypeError somewhere.")
            pass
        except AttributeError:
            print("Warning: You're getting an Attribute Error somewhere.")
            pass

IA = IA()


if DEBUG == False :
    speak("Démarrage IA réussi. à l'écoute")
    while True:
        command = IA.hear(recognizer, microphone)
        IA.analyze(command)
    
else :
    Analyze_text("quel temps fait il")
