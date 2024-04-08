import os
import subprocess
import speech_recognition as sr
import pyttsx3

def process_command(command):
    key_words = ['найти', 'найди', 'поиск', 'открыть', 'запустить',  'закрыть', 'видео', 'discord'] 
    search_query = ""
    
    for word in key_words:
        if word in command.lower():
            search_query = command.replace(word, "")
            break
    
    search_query = search_query.strip().replace(" ", "+")
    
    
    if 'видео' in command.lower():
        search_query = command.replace('видео', "")
        search_query = search_query.strip().replace(" ", "+")
        chrome_path = "\"C:/Program Files/Google/Chrome/Application/chrome.exe\" %s"
        url = "https://www.youtube.com/results?search_query=" + search_query
        subprocess.Popen(chrome_path % url, shell=True)
    elif 'discord' in command.lower(): 
        os.startfile("C:/Users/Пользователь/AppData/Local/Discord/app-1.0.9039/Discord.exe") # Путь к исполняемому файлу Discord
    elif 'найти' in command.lower() or 'найди' in command.lower() or 'поиск' in command.lower(): 
        chrome_path = "\"C:/Program Files/Google/Chrome/Application/chrome.exe\" %s"
        url = "https://www.google.com/search?q=" + search_query
        subprocess.Popen(chrome_path % url, shell=True)
    

def record_command():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        engine.say("Говорите...")
        engine.runAndWait()
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="ru-RU")
        engine.say("Вы сказали: " + command)
        engine.runAndWait()
        return command
    except sr.UnknownValueError:
        engine.say("Произнесенная речь не распознана")
        engine.runAndWait()
        return ""
    except sr.RequestError as e:
        engine.say("Ошибка сервиса распознавания речи")
        engine.runAndWait()
        return ""

if __name__ == "__main__":
    command = record_command()
    if command:
        process_command(command)
