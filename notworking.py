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

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Ready to comply. What can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def handle_commands(query):


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
        qrry = takeCommand().lower()
        kit.playonyt(f"{qrry}")
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
    elif 'close youtube' in query:
        os.system("taskkill /f /im msedge.exe")
    elif 'open google' in query:
        speak("What should I search?")
        qry = takeCommand().lower()
        webbrowser.open(f"{qry}")
    elif 'close google' in query:
        os.system("taskkill /f /im msedge.exe")
    elif 'play music' in query:
        music_dir = 'E:\\Musics'
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
        name = takeCommand().lower()
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
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                'divided': operator.__truediv__,
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
        response = 'My name is Stewie. I can do everything that my creator programmed me to do.'
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

def chrome_automation(query):
    if 'open chrome' in query:
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'maximize this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
    elif 'google search' in query:
        query = query.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'youtube search' in query:
        query = query.replace("youtube search", "")
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        pyautogui.press('tab', presses=4)
        time.sleep(1)
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'open new window' in query:
        pyautogui.hotkey('ctrl', 'n')
    elif 'open incognito window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')
    elif 'minimise this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
    elif 'open history' in query:
        pyautogui.hotkey('ctrl', 'h')
    elif 'open downloads' in query:
        pyautogui.hotkey('ctrl', 'j')
    elif 'previous tab' in query:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    elif 'next tab' in query:
        pyautogui.hotkey('ctrl', 'tab')
    elif 'close tab' in query:
        pyautogui.hotkey('ctrl', 'w')
    elif 'close window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'w')
    elif 'clear browsing history' in query:
        pyautogui.hotkey('ctrl', 'shift', 'delete')
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")

def image_recognition(query):
    if 'open chrome' in query:
        img = pyautogui.locateCenterOnScreen('Screenshot1.png')
        pyautogui.doubleClick(img)
        time.sleep(1)
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
        time.sleep(1)
        img1 = pyautogui.locateCenterOnScreen('screenshot2.png')
        pyautogui.click(img1)
        time.sleep(2)
        img2 = pyautogui.locateCenterOnScreen('screenshot3.png')
        pyautogui.click(img2)
        time.sleep(1)
        pyautogui.typewrite('How To Manual', 0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
        pyautogui.click(img3)
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
    #OPENAI key issue_________________________________________________________________________________________!
    elif 'weather' in query:
        speak("Which city would you like to know the weather for?")
        city = takeCommand().lower()
        try:
            api_key = "YOUR_API_KEY"  # OpenWeatherMap API key
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            speak(f"The temperature in {city} is {temp}°C with {desc}")
        except:
            speak("Sorry, I couldn't fetch the weather information")

    elif 'set reminder' in query:
        speak("What should I remind you about?")
        reminder_text = takeCommand().lower()
        speak("In how many minutes?")
        minutes = int(takeCommand().lower())
        def remind():
            speak(f"Reminder: {reminder_text}")
        import threading
        timer = threading.Timer(minutes * 60, remind)
        timer.start()
        speak(f"Reminder set for {minutes} minutes from now")

    elif 'system info' in query:
        import psutil
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        speak(f"CPU usage is {cpu}%, Memory usage is {memory}%, and Disk usage is {disk}%")

    elif 'news headlines' in query:
        try:
            news_api_key = "YOUR_NEWS_API_KEY"
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
            news = requests.get(url).json()
            for i, article in enumerate(news['articles'][:5]):
                speak(f"Headline {i+1}: {article['title']}")
        except:
            speak("Sorry, I couldn't fetch the news")

    elif 'convert currency' in query:
        speak("Enter amount")
        amount = float(takeCommand())
        speak("From which currency? (e.g., USD)")
        from_currency = takeCommand().upper()
        speak("To which currency? (e.g., EUR)")
        to_currency = takeCommand().upper()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][to_currency]
        converted = amount * rate
        speak(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")

    elif 'create text file' in query:
        speak("What should I write in the file?")
        content = takeCommand()
        speak("What should be the file name?")
        filename = takeCommand().lower().replace(" ", "_") + ".txt"
        with open(filename, 'w') as f:
            f.write(content)
        speak(f"File {filename} has been created")

    elif 'battery status' in query:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        speak(f"Battery is at {percent}% and {'plugged in' if plugged else 'not plugged in'}")

    elif 'set timer' in query:
        speak("For how many seconds?")
        seconds = int(takeCommand())
        speak(f"Timer set for {seconds} seconds")
        time.sleep(seconds)
        speak("Time's up!")

    elif 'read pdf' in query:
        import PyPDF2
        speak("What's the name of the PDF file?")
        pdf_name = takeCommand().lower() + ".pdf"
        try:
            book = open(pdf_name, 'rb')
            pdfReader = PyPDF2.PdfReader(book)
            pages = len(pdfReader.pages)
            speak(f"Total pages in the PDF are {pages}")
            speak("Which page should I read?")
            pg = int(takeCommand())
            page = pdfReader.pages[pg-1]
            text = page.extract_text()
            speak(text)
        except:
            speak("Couldn't find or read the PDF file")

    elif 'media control' in query:
        if 'pause' in query:
            pyautogui.press('playpause')
        elif 'next' in query:
            pyautogui.press('nexttrack')
        elif 'previous' in query:
            pyautogui.press('prevtrack')

    elif 'send email' in query:
        import smtplib
        speak("What's the recipient's email?")
        to = takeCommand().lower().replace(" ", "")
        speak("What's the subject?")
        subject = takeCommand()
        speak("What's the message?")
        message = takeCommand()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail("your_email@gmail.com", to, email_message)
            server.quit()
            speak("Email has been sent")
        except:
            speak("Couldn't send the email")

    elif 'clean system' in query:
        import shutil
        try:
            os.system('del /f /s /q %temp%/*')
            shutil.rmtree(os.path.expanduser('~/.recycle-bin'), ignore_errors=True)
            speak("System cleanup completed")
        except:
            speak("Couldn't complete system cleanup")

    elif 'take notes' in query:
        speak("What should I note down?")
        note_text = takeCommand()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"note_{timestamp}.txt", "w") as f:
            f.write(note_text)
        speak("Note has been saved")

    elif 'define word' in query:
        from PyDictionary import PyDictionary
        dictionary = PyDictionary()
        speak("What word would you like me to define?")
        word = takeCommand().lower()
        meaning = dictionary.meaning(word)
        if meaning:
            speak(f"The definition of {word} is: {meaning}")
        else:
            speak("Sorry, I couldn't find the definition")

    elif 'calendar events' in query:
        from datetime import date
        today = date.today()
        speak(f"Today is {today.strftime('%B %d, %Y')}")
        # calendar API integration left

    elif 'network speed' in query:
        import speedtest
        speak("Testing internet speed...")
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000
        speak(f"Download speed is {download_speed:.2f} Mbps")
        speak(f"Upload speed is {upload_speed:.2f} Mbps")

    elif 'start screen recording' in query:
        import cv2
        import numpy as np
        from PIL import ImageGrab
        speak("Screen recording started. Say 'stop recording' to end.")
        filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".avi"
        screen = np.array(ImageGrab.grab())
        height, width, _ = screen.shape
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))
        while True:
            if 'stop recording' in query:
                break
            frame = np.array(ImageGrab.grab())
            out.write(frame)
        out.release()
        speak("Screen recording saved")

    elif 'organize files' in query:
        speak("Which directory should I organize?")
        dir_path = takeCommand()
        extensions = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt'],
            'Videos': ['.mp4', '.avi', '.mkv'],
            'Music': ['.mp3', '.wav']
        }
        for filename in os.listdir(dir_path):
            for category, exts in extensions.items():
                if any(filename.lower().endswith(ext) for ext in exts):
                    category_path = os.path.join(dir_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    os.rename(
                        os.path.join(dir_path, filename),
                        os.path.join(category_path, filename)
                    )
        speak("Files have been organized")

    elif 'check website' in query:
        speak("What website should I check?")
        website = takeCommand().lower()
        if not website.startswith('http'):
            website = 'http://' + website
        try:
            response = requests.get(website)
            if response.status_code == 200:
                speak("Website is up and running")
            else:
                speak("Website might be having issues")
        except:
            speak("Couldn't reach the website")

    elif 'backup files' in query:
        speak("Which directory should I backup?")
        source_dir = takeCommand()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"backup_{timestamp}"
        try:
            shutil.copytree(source_dir, backup_dir)
            speak("Backup completed successfully")
        except:
            speak("Couldn't complete the backup")
    elif 'find file' in query:
        speak("What's the name of the file?")
        filename = takeCommand().lower()
        speak("In which drive should I search? For example, C or D")
        drive = takeCommand().upper() + ":\\"
        def find_file(filename, search_path):
            result = []
            for root, dir, files in os.walk(search_path):
                if any(filename in file.lower() for file in files):
                    result.append(root)
            return result
        speak("Searching... This might take a moment")
        locations = find_file(filename, drive)
        if locations:
            speak(f"Found {filename} in the following locations:")
            for loc in locations:
                speak(loc)
        else:
            speak("File not found")

    elif 'calculator' in query:
        speak("What type of calculation? Say add, subtract, multiply, or divide")
        op = takeCommand().lower()
        speak("First number")
        num1 = float(takeCommand())
        speak("Second number")
        num2 = float(takeCommand())
        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        speak(f"The result is {result}")

    elif 'morse code' in query:
        morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----'}
        speak("What text should I convert to Morse code?")
        text = takeCommand().upper()
        morse = ' '.join(morse_dict.get(char, '') for char in text)
        speak("Here's your Morse code")
        print(morse)
        speak(morse.replace('.', 'dot').replace('-', 'dash'))

    elif 'monitor system' in query:
        import psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        speak(f"CPU Usage: {cpu_percent}% Memory Used: {memory.percent}% Disk Usage: {disk.percent}% Available Memory: {memory.available / (1024 * 1024 * 1024):.2f} GB")

    # elif 'encrypt file' in query or 'decrypt file' in query:
    #     from cryptography.fernet import Fernet
    #     def generate_key():
    #         return Fernet.generate_key()
    #     def encrypt_file(filename, key):
    #         f = Fernet(key)
    #         with open(filename, 'rb') as file:
    #             file_data = file.read()
    #         encrypted_data = f.encrypt(file_data)
    #         with open(filename + '.encrypted', 'wb') as file:
    #             file.write(encrypted_data)
    #     speak("Enter the file path")
    #     file_path = takeCommand()
    #     if os.path.exists(file_path):
    #         key = generate_key()
    #         with open('filekey.key', 'wb') as filekey:
    #             filekey.write(key)
    #         encrypt_file(file_path, key)
    #         speak("File encrypted successfully")
    #     else:
    #         speak("File not found")

    elif 'generate password' in query:
        import random, string
        speak("How many characters should the password be?")
        length = int(takeCommand())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        speak("Here's your generated password")
        print(password)
        pyautogui.write(password)

    elif 'analyze text' in query:
        speak("Please say the text you want to analyze")
        text = takeCommand()
        words = len(text.split())
        chars = len(text)
        sentences = len(text.split('.'))
        speak(f"Number of words: {words} Number of characters: {chars} Number of sentences: {sentences} Average word length: {chars/words:.2f} characters")

    elif 'show directory tree' in query:
        speak("Which directory should I analyze?")
        path = takeCommand()
        def display_tree(startpath):
            for root, dirs, files in os.walk(startpath):
                level = root.replace(startpath, '').count(os.sep)
                indent = ' ' * 4 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f"{subindent}{f}")
        display_tree(path)
        speak("Directory tree generated")

    elif 'clipboard history' in query:
        import pyperclip
        clipboard_history = []
        speak("Clipboard manager activated. Say 'stop clipboard' to end")
        while True:
            current = pyperclip.paste()
            if current not in clipboard_history:
                clipboard_history.append(current)
            if 'stop clipboard' in query:
                break
        speak("Here's your clipboard history")
        for item in clipboard_history:
            print(item)
            speak(item)

    elif 'show progress' in query:
        speak("How many seconds should the task take?")
        duration = int(takeCommand())
        from tqdm import tqdm
        for _ in tqdm(range(duration)):
            time.sleep(1)
        speak("Task completed")

    elif 'find duplicates' in query:
        import hashlib
        def get_file_hash(filepath):
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        speak("Which directory should I check?")
        directory = takeCommand()
        hash_dict = {}
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = get_file_hash(filepath)
                if file_hash in hash_dict:
                    speak(f"Duplicate found: {filepath} and {hash_dict[file_hash]}")
                else:
                    hash_dict[file_hash] = filepath

    elif 'detailed system info' in query:
        import platform
        system_info = {
            'System': platform.system(),
            'Node Name': platform.node(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Machine': platform.machine(),
            'Processor': platform.processor()
        }
        for key, value in system_info.items():
            speak(f"{key}: {value}")

    elif 'count file types' in query:
        speak("Which directory should I analyze?")
        directory = takeCommand()
        extension_count = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                extension_count[ext] = extension_count.get(ext, 0) + 1
        speak("Here are the file types and their counts:")
        for ext, count in extension_count.items():
            speak(f"{ext or 'No extension'}: {count} files")

    elif 'countdown' in query:
        import winsound
        speak("How many seconds to countdown?")
        seconds = int(takeCommand())
        for i in range(seconds, 0, -1):
            print(i)
            time.sleep(1)
        winsound.Beep(1000, 1000)
        speak("Countdown finished!")

    elif 'convert to binary' in query:
        speak("What text should I convert to binary?")
        text = takeCommand()
        binary = ' '.join(format(ord(char), '08b') for char in text)
        speak("Here's your text in binary")
        print(binary)

    elif 'show processes' in query:
        import psutil
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            processes.append(proc.info)
        sorted_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:10]
        speak("Top 10 processes by memory usage:")
        for proc in sorted_processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}, Memory: {proc['memory_percent']:.2f}%")

    elif 'calculate folder size' in query:
        speak("Which folder should I analyze?")
        folder_path = takeCommand()
        def get_size(start_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(start_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size
        size = get_size(folder_path)
        speak(f"The total size is {size / (1024 * 1024):.2f} MB")

    elif 'quick note' in query:
        notes_file = "quick_notes.txt"
        speak("What would you like to note down?")
        note = takeCommand()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(notes_file, "a") as f:
            f.write(f"\n[{timestamp}]\n{note}\n")
        speak("Note saved")

    elif 'keyboard shortcuts' in query:
        import keyboard
        speak("Keyboard shortcut manager activated. Say 'stop shortcuts' to end")
        recorded = keyboard.record(until='esc')
        speak("Here are your recorded keystrokes:")
        print(keyboard.get_typewriter_input(recorded))

    elif 'monitor folder' in query:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        class MyHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if not event.is_directory:
                    speak(f"File {event.src_path} has been modified")
            def on_created(self, event):
                if not event.is_directory:
                    speak(f"File {event.src_path} has been created")
            def on_deleted(self, event):
                if not event.is_directory:
                    speak(f"File {event.src_path} has been deleted")
        speak("Which folder should I monitor?")
        path = takeCommand()
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()
        speak("Monitoring started. Say 'stop monitoring' to end")
        try:
            while True:
                if 'stop monitoring' in query:
                    observer.stop()
                    break
        except:
            observer.stop()
        observer.join()

    elif 'compress files' in query:
        import zipfile
        speak("Which folder should I compress?")
        folder_to_zip = takeCommand()
        speak("Name for the zip file?")
        zip_name = takeCommand() + ".zip"
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_to_zip):
                for file in files:
                    zipf.write(os.path.join(root, file))
        speak("Compression complete")

    elif 'extract zip' in query:
        import zipfile
        speak("Path to the zip file?")
        zip_path = takeCommand()
        speak("Extraction directory?")
        extract_path = takeCommand()
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        speak("Extraction complete")

    elif 'create qr code' in query:
        import qrcode
        speak("What text or URL should I encode?")
        data = takeCommand()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")
        speak("QR code generated")

    elif 'text similarity' in query:
        from difflib import SequenceMatcher
        speak("Enter first text")
        text1 = takeCommand()
        speak("Enter second text")
        text2 = takeCommand()
        similarity = SequenceMatcher(None, text1, text2).ratio()
        speak(f"The texts are {similarity * 100:.2f}% similar")

    elif 'word count' in query:
        speak("Enter text to count words")
        text = takeCommand()
        word_count = {}
        for word in text.lower().split():
            word_count[word] = word_count.get(word, 0) + 1
        speak("Here are the word frequencies:")
        for word, count in word_count.items():
            speak(f"{word}: {count} times")

    elif 'backup directory' in query:
        import shutil
        speak("Which directory to backup?")
        src_dir = takeCommand()
        backup_dir = src_dir + "_backup"
        shutil.copytree(src_dir, backup_dir)
        speak("Backup created")

    elif 'check disk space' in query:
        import shutil
        disk = shutil.disk_usage("/")
        total = disk.total / (2**30)
        used = disk.used / (2**30)
        free = disk.free / (2**30)
        speak(f"Total: {total:.1f} GB, Used: {used:.1f} GB, Free: {free:.1f} GB")

    elif 'system temperature' in query:
        import psutil
        try:
            temps = psutil.sensors_temperatures()
            for name, entries in temps.items():
                for entry in entries:
                    speak(f"{name}: {entry.current}°C")
        except:
            speak("Temperature sensors not available")

    elif 'monitor network' in query:
        import psutil
        old_value = psutil.net_io_counters()
        time.sleep(1)
        new_value = psutil.net_io_counters()
        speak(f"Download Speed: {(new_value.bytes_recv - old_value.bytes_recv) / 1024 / 1024:.2f} MB/s")
        speak(f"Upload Speed: {(new_value.bytes_sent - old_value.bytes_sent) / 1024 / 1024:.2f} MB/s")
        elif 'find file' in query:
        speak("What's the name of the file?")
        filename = takeCommand().lower()
        speak("In which drive should I search? For example, C or D")
        drive = takeCommand().upper() + ":\\"

        def find_file(filename, search_path):
            result = []
            for root, dir, files in os.walk(search_path):
                if any(filename in file.lower() for file in files):
                    result.append(root)
            return result

        speak("Searching... This might take a moment")
        locations = find_file(filename, drive)
        if locations:
            speak(f"Found {filename} in the following locations:")
            for loc in locations:
                speak(loc)
        else:
            speak("File not found")

    elif 'calculator' in query:
        speak("What type of calculation? Say add, subtract, multiply, or divide")
        op = takeCommand().lower()
        speak("First number")
        num1 = float(takeCommand())
        speak("Second number")
        num2 = float(takeCommand())

        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        speak(f"The result is {result}")

    elif 'morse code' in query:
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----'
        }
        speak("What text should I convert to Morse code?")
        text = takeCommand().upper()
        morse = ' '.join(morse_dict.get(char, '') for char in text)
        speak("Here's your Morse code")
        print(morse)
        speak(morse.replace('.', 'dot').replace('-', 'dash'))

    elif 'monitor system' in query:
        import psutil
        speak("Monitoring system resources")
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        speak(f"""
            CPU Usage: {cpu_percent}%
            Memory Used: {memory.percent}%
            Disk Usage: {disk.percent}%
            Available Memory: {memory.available / (1024 * 1024 * 1024):.2f} GB
        """)

    # elif 'encrypt file' in query or 'decrypt file' in query:
    #     from cryptography.fernet import Fernet

    #     def generate_key():
    #         return Fernet.generate_key()

    #     def encrypt_file(filename, key):
    #         f = Fernet(key)
    #         with open(filename, 'rb') as file:
    #             file_data = file.read()
    #         encrypted_data = f.encrypt(file_data)
    #         with open(filename + '.encrypted', 'wb') as file:
    #             file.write(encrypted_data)

        # speak("Enter the file path")
        # file_path = takeCommand()
        # if os.path.exists(file_path):
        #     key = generate_key()
        #     with open('filekey.key', 'wb') as filekey:
        #         filekey.write(key)
        #     encrypt_file(file_path, key)
        #     speak("File encrypted successfully")
        # else:
        #     speak("File not found")

    elif 'generate password' in query:
        import random
        import string
        speak("How many characters should the password be?")
        length = int(takeCommand())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        speak("Here's your generated password")
        print(password)
        pyautogui.write(password)

    elif 'analyze text' in query:
        speak("Please say the text you want to analyze")
        text = takeCommand()
        words = len(text.split())
        chars = len(text)
        sentences = len(text.split('.'))
        speak(f"""
            Number of words: {words}
            Number of characters: {chars}
            Number of sentences: {sentences}
            Average word length: {chars/words:.2f} characters
        """)

    elif 'show directory tree' in query:
        speak("Which directory should I analyze?")
        path = takeCommand()

        def display_tree(startpath):
            for root, dirs, files in os.walk(startpath):
                level = root.replace(startpath, '').count(os.sep)
                indent = ' ' * 4 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f"{subindent}{f}")

        display_tree(path)
        speak("Directory tree generated")

    elif 'clipboard history' in query:
        import pyperclip
        clipboard_history = []
        speak("Clipboard manager activated. Say 'stop clipboard' to end")
        while True:
            current = pyperclip.paste()
            if current not in clipboard_history:
                clipboard_history.append(current)
            if 'stop clipboard' in query:
                break
        speak("Here's your clipboard history")
        for item in clipboard_history:
            print(item)
            speak(item)

    elif 'show progress' in query:
        speak("How many seconds should the task take?")
        duration = int(takeCommand())
        from tqdm import tqdm
        import time
        for _ in tqdm(range(duration)):
            time.sleep(1)
        speak("Task completed")

    elif 'find duplicates' in query:
        import hashlib

        def get_file_hash(filepath):
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()

        speak("Which directory should I check?")
        directory = takeCommand()
        hash_dict = {}

        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = get_file_hash(filepath)
                if file_hash in hash_dict:
                    speak(f"Duplicate found: {filepath} and {hash_dict[file_hash]}")
                else:
                    hash_dict[file_hash] = filepath

    elif 'detailed system info' in query:
        import platform
        system_info = {
            'System': platform.system(),
            'Node Name': platform.node(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Machine': platform.machine(),
            'Processor': platform.processor()
        }
        for key, value in system_info.items():
            speak(f"{key}: {value}")

    elif 'count file types' in query:
        speak("Which directory should I analyze?")
        directory = takeCommand()
        extension_count = {}

        for root, dirs, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                extension_count[ext] = extension_count.get(ext, 0) + 1

        speak("Here are the file types and their counts:")
        for ext, count in extension_count.items():
            speak(f"{ext or 'No extension'}: {count} files")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        handle_commands(query)
        chrome_automation(query)
        image_recognition(query)
