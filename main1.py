from __future__ import with_statement 
import pyttsx3  
import speech_recognition as sr  
import datetime 
import wikipedia 
import webbrowser 
import os 
import random 
import cv2 
import pywhatkit as kit 
import sys 
import pyautogui 
import time 
import operator 
import requests 
import pyaudio
import subprocess
import json
import wolframalpha
from win10toast import ToastNotifier
import pyjokes
import psutil
import speedtest
import screen_brightness_control as sbc
import python_weather as wf
import pytube
import qrcode
from win10toast import ToastNotifier
from wordnik import swagger, WordApi
from countryinfo import CountryInfo
import ascii_magic
from covid19 import COVID19
from translate import Translator
from newsapi import NewsApiClient
import geocoder
import forex_python.converter
import platform
from pycoingecko import CoinGeckoAPI
import nltk
from nltk.corpus import wordnet

# Constants
WAKE_WORD = "jarvis"
USERNAME = "Sir"  # or whatever name you prefer
MUSIC_DIR = "D:\\Songs"  # Replace with your music directory path

p = pyaudio.PyAudio()
print("Available input devices:")
for i in range(p.get_device_count()):
    print(f"{i}: {p.get_device_info_by_index(i)['name']}")

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 150) 

# Initialize recognizer
r = sr.Recognizer()

# Define paths and API keys
browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
search_url = "https://www.google.com/search?q="
youtube_url = "https://www.youtube.com/results?search_query="
weather_api_key = "YOUR_WEATHER_API_KEY"  # Replace with your actual API key
wolframalpha_app_id = "YOUR_WOLFRAMALPHA_APP_ID"  # Replace with your actual App ID

# Initialize WolframAlpha client
wolframalpha_client = wolframalpha.Client(wolframalpha_app_id)

# # Replace PyDictionary initialization with Wordnik
# wordnik_client = swagger.ApiClient('YOUR-WORDNIK-API-KEY', 'http://api.wordnik.com/v4')
# word_api = WordApi.WordApi(wordnik_client)

# Add this with other client initializations
news_client = NewsApiClient(api_key='YOUR-NEWS-API-KEY')  # Replace with your actual API key
cg = CoinGeckoAPI()  # Add this near other client initializations

# Initialize notification
toaster = ToastNotifier()  # Add this with other initializations

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    mic_index = 2  # Index for Microphone (USB PnP Audio Device)
    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Add timeout
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand audio, please try again.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "None"
    return query


# def takeCommand(): 
#     r = sr.Recognizer() 
#     with sr.Microphone() as source: 
#         print("Listening...") 
#         r.pause_threshold = 1 
#         try:
#             audio = r.listen(source) 
#             print("Recognizing...")     
#             query = r.recognize_google(audio, language='en-in') 
#             print(f"User said: {query}\n") 
#         except Exception as e:     
#             print("Say that again please...")   
#             return "None" 
#     return query 

if __name__ == "__main__": 
    wishMe() 
    while True: 
        query = takeCommand() 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
        elif "channel analytics" in query: 
            webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default") 
        elif 'search on youtube' in query: 
            query = query.replace("search on youtube", "") 
            webbrowser.open(f"www.youtube.com/results?search_query={query}") 
        elif 'open youtube' in query: 
            speak("What would you like to watch?") 
            qrry = takeCommand() 
            kit.playonyt(f"{qrry}") 
        elif 'close chrome' in query: 
            os.system("taskkill /f /im chrome.exe") 
        elif 'close youtube' in query: 
            os.system("taskkill /f /im msedge.exe") 
        elif 'open google' in query: 
            speak("What should I search?") 
            qry = takeCommand() 
            webbrowser.open(f"{qry}") 
        elif 'close google' in query: 
            os.system("taskkill /f /im msedge.exe") 
        elif 'play music' in query: 
            music_dir = MUSIC_DIR 
            songs = os.listdir(music_dir)     
            os.startfile(os.path.join(music_dir, random.choice(songs))) 
        elif 'play iron man movie' in query: 
            npath = "E:\\ironman.mkv"     
            os.startfile(npath) 
        elif 'close movie' in query or 'close music' in query: 
            os.system("taskkill /f /im vlc.exe") 
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}") 
        elif "shut down the system" in query: 
            os.system("shutdown /s /t 5") 
        elif "restart the system" in query: 
            os.system("shutdown /r /t 5") 
        elif "lock the system" in query: 
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
        elif "close notepad" in query: 
            os.system("taskkill /f /im notepad.exe") 
        elif "open command prompt" in query: 
            os.system("start cmd") 
        elif "close command prompt" in query: 
            os.system("taskkill /f /im cmd.exe") 
        elif "open camera" in query: 
            cap = cv2.VideoCapture(0) 
            while True: 
                ret, img = cap.read() 
                cv2.imshow('webcam', img) 
                k = cv2.waitKey(50) 
                if k == 27: 
                    break 
            cap.release() 
            cv2.destroyAllWindows() 
        elif "go to sleep" in query: 
            speak('Alright then, I am switching off') 
            sys.exit() 
        elif "take screenshot" in query: 
            speak('Tell me a name for the file') 
            name = takeCommand() 
            time.sleep(3) 
            img = pyautogui.screenshot()   
            img.save(f"{name}.png")   
            speak("Screenshot saved") 
        elif "calculate" in query: 
            r = sr.Recognizer() 
            with sr.Microphone() as source: 
                speak("Ready") 
                print("Listening...") 
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
                my_string = r.recognize_google(audio) 
                print(my_string) 
            def get_operator_fn(op): 
                return { 
                    '+' : operator.add, 
                    '-' : operator.sub, 
                    'x' : operator.mul, 
                    'divided' : operator.__truediv__, 
                }.get(op) 
            def eval_binary_expr(op1, oper, op2): 
                op1, op2 = int(op1), int(op2) 
                return get_operator_fn(oper)(op1, op2) 
            speak("Your result is") 
            speak(eval_binary_expr(*(my_string.split()))) 
        elif "what is my ip address" in query: 
            speak("Checking") 
            try: 
                ipAdd = requests.get('https://api.ipify.org').text 
                print(ipAdd) 
                speak("Your IP address is") 
                speak(ipAdd) 
            except Exception as e: 
                speak("Network is weak, please try again some time later") 
        elif "volume up" in query: 
            for _ in range(15): 
                pyautogui.press("volumeup") 
        elif "volume down" in query: 
            for _ in range(15): 
                pyautogui.press("volumedown") 
        elif "mute" in query: 
            pyautogui.press("volumemute") 
        elif "refresh" in query: 
            pyautogui.moveTo(1551, 551, 2) 
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right') 
            pyautogui.moveTo(1620, 667, 1) 
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left') 
        elif "scroll down" in query: 
            pyautogui.scroll(-1000) 
        elif "drag visual studio to the right" in query: 
            pyautogui.moveTo(46, 31, 2) 
            pyautogui.dragRel(1857, 31, 2) 
        elif "rectangular spiral" in query: 
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('paint') 
            time.sleep(1) 
            pyautogui.press('enter') 
            time.sleep(1) 
            pyautogui.moveTo(100, 193, 1) 
            pyautogui.rightClick() 
            distance = 300 
            while distance > 0: 
                pyautogui.dragRel(distance, 0, 0.1, button="left") 
                distance = distance - 10 
                pyautogui.dragRel(0, distance, 0.1, button="left") 
                pyautogui.dragRel(-distance, 0, 0.1, button="left") 
                distance = distance - 10 
                pyautogui.dragRel(0, -distance, 0.1, button="left") 
        elif "close paint" in query: 
            os.system("taskkill /f /im mspaint.exe") 
        elif "who are you" in query: 
            response = 'My name is Six. I can do everything that my creator programmed me to do.' 
            print(response) 
            speak(response) 
        elif "who created you" in query: 
            response = 'I do not know his name. I was created with Python language, in Visual Studio Code.' 
            print(response) 
            speak(response) 
        elif "open notepad and write my channel name" in query: 
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('notepad') 
            time.sleep(1) 
            pyautogui.press('enter') 
            time.sleep(1) 
            pyautogui.write("How To Manual", interval = 0.1) 
        elif "subscribe" in query: 
            response = "Everyone who is watching this, please subscribe to our channel How To Manual for interesting tutorials and information. Thanks for watching." 
            print(response) 
            speak(response) 
        elif 'type' in query: 
            query = query.replace("type", "") 
            pyautogui.write(f"{query}") 
        elif "system stats" in query:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            speak(f"CPU usage is {cpu}percent, Memory usage is {memory}percent, and Disk usage is {disk}percent")

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            speak("Testing download speed...")
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            speak(f"Download speed is {round(download_speed, 2)} Megabits per second")

        elif "adjust brightness" in query:
            speak("What percentage brightness would you like?")
            try:
                brightness = int(takeCommand())
                sbc.set_brightness(brightness)
                speak(f"Brightness set to {brightness} percent")
            except:
                speak("Sorry, I couldn't adjust the brightness")

        elif "copy text" in query:
            pyautogui.hotkey('ctrl', 'c')
            speak("Text copied to clipboard")

        elif "paste text" in query:
            pyautogui.hotkey('ctrl', 'v')
            speak("Text pasted")

        elif "weather" in query:
            speak("Which city?")
            city = takeCommand()
            weather = wf.forecast(place=city, time=datetime.datetime.now())
            speak(f"The temperature in {city} is {weather.temperature} degrees")

        elif "download youtube video" in query:
            speak("Please provide the YouTube URL")
            url = takeCommand()
            try:
                yt = pytube.YouTube(url)
                video = yt.streams.get_highest_resolution()
                video.download()
                speak("Video downloaded successfully")
            except:
                speak("Sorry, couldn't download the video")

        elif "generate qr code" in query:
            speak("What would you like to encode in the QR code?")
            data = takeCommand()
            img = qrcode.make(data)
            img.save("qr_code.png")
            speak("QR code generated and saved")

        elif "country information" in query:
            speak("Which country would you like to know about?")
            country = takeCommand()
            try:
                country_info = CountryInfo(country)
                capital = country_info.capital()
                population = country_info.population()
                speak(f"The capital of {country} is {capital} and its population is {population}")
            except:
                speak("Sorry, I couldn't find information about that country")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "system notification" in query:
            speak("What should the notification say?")
            message = takeCommand()
            toaster.show_toast("Assistant", message, duration=5)

        # elif "dictionary" in query:
        #     speak("What word would you like to look up?")
        #     word = takeCommand()
        #     meaning = word_api.getDefinitions(word)
        #     speak(f"The meaning of {word} is {meaning}")

        elif "covid stats" in query:
            speak("Which country's COVID stats would you like to know?")
            country = takeCommand()
            covid_data = COVID19()
            stats = covid_data.get_status_by_country_name(country)
            speak(f"Total cases in {country} are {stats['confirmed']}")

        elif "create ascii art" in query:
            speak("I'll convert your last screenshot to ASCII art")
            ascii_magic.from_image_file("screenshot.png").to_terminal()

        elif "translate" in query:
            speak("What would you like to translate?")
            text = takeCommand()
            speak("To which language? Please specify the language code")
            lang = takeCommand()
            translator = Translator(to_lang=lang)
            translation = translator.translate(text)
            speak(f"The translation is: {translation}")

        elif "bitcoin price" in query:
            price = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
            speak(f"The current Bitcoin price is {price} US dollars")

        elif "latest news" in query:
            news = news_client.get_top_headlines(language='en', country='us')
            for article in news['articles'][:3]:
                speak(article['title'])

        elif "do math" in query:
            speak("What's your question?")
            question = takeCommand()
            res = wolframalpha_client.query(question)
            try:
                speak(next(res.results).text)
            except:
                speak("Sorry, I couldn't solve that")

        elif "currency convert" in query:
            c = forex_python.converter.CurrencyRates()
            speak("From which currency?")
            from_currency = takeCommand().upper()
            speak("To which currency?")
            to_currency = takeCommand().upper()
            speak("Amount?")
            amount = float(takeCommand())
            result = c.convert(from_currency, to_currency, amount)
            speak(f"{amount} {from_currency} is {result} {to_currency}")

        elif "my location" in query:
            g = geocoder.ip('me')
            speak(f"Your current location is {g.city}, {g.country}")

        elif "system information" in query:
            system_info = platform.uname()
            speak(f"You are running {system_info.system} version {system_info.version}")