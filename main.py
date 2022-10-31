import pyttsx3 
from speech_recognition import Recognizer, Microphone
import webbrowser
import datetime
import wikipedia
from random import *

global engine
engine = pyttsx3.init()
voices = "italian"
engine.setProperty('voice', voices)

global nameAssistant
nameAssistant = "jarvis"
global nameUser
nameUser = "Daniel"

global speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe(*args):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buongiorno!")
    elif hour>=12 and hour<18:
        speak("Buon pomeriggio!")   
    else:
        speak("Buonasera!")  
    speak(f"Sono {nameAssistant}.")

def sayHour(*args):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sono le {strTime}")

def sayDate(*args):
    strDate = datetime.datetime.now().strftime("%d/%m/%Y")
    speak(f"Oggi è il {strDate}")

def sayDay(*args):
    strDay = datetime.datetime.now().strftime("%A")
    speak(f"Oggi è {strDay}")

def sayJoke(*args):
    strJoke = choice(["Qual è il colmo per un informatico? Non avere un backup.", "Nuova ipotesi scientifica sul BIG BANG: Dio digito 'Pkunzip universo'.", "Quanti programmatori ci vogliono per avvitare una lampadina? Nessuno, e' un problema hardware!", "Ho provato a installare troppi sistemi operativi sul mio PC! E' andato in overdos", "Quando il gioco si fa duro, i duri resettano il sistema."])
    speak(strJoke)

def sayNameU(*args):
    speak(f"Ti chiami {nameUser}")

def doSearch(quer, *args):
    speak("Sto cercando...")
    query = quer.replace("cerca", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def doWikipedia(query, *args):
    speak("Sto cercando su wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak("Secondo Wikipedia")
    speak(results)

def doYouTube(query, *args):
    speak("Sto cercando...")
    query = query.replace("youtube", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def takeCommand():
    r = Recognizer()
    with Microphone() as source:
        print("Ascolto...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Riconoscimento...")
        query = r.recognize_google(audio, language='it-IT').lower()
        print(f"Utente: {query}\n")
    except Exception as e:
        print(e)
        print("Ripeti, per favore...")
        speak("Ripeti, per favore...")
        return "None"
    return query

while True:
    jarvis = takeCommand().lower()
    if jarvis in nameAssistant:
        speak("Come posso aiutarti?")
        query = takeCommand().lower()
        if 'ciao' in query:
            wishMe()
        elif 'ora' in query:
            sayHour()
        elif 'data' in query:
            sayDate()
        elif 'giorno' in query:
            sayDay()
        elif 'barzelletta' in query:
            sayJoke()
        elif 'nome' in query:
            sayNameU()
        elif 'cerca' in query:
            print(query)
            doSearch(query)
        elif 'wikipedia' in query:
            doWikipedia(query)
        elif 'youtube' in query:
            doYouTube(query)

