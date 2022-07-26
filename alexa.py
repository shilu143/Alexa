import speech_recognition as sr
import pyttsx3
import datetime
import os
# import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import geocoder


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'am Alexa, how can I help you.")


def currWeather():
    g = geocoder.ip('me')
    lat = str(g.latlng[0])
    lon = str(g.latlng[1])
    apiKey = "920f29efb70eadb7f5d5efa8977112d2"             

    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat
    api_url += "&lon="
    api_url += lon
    api_url += "&units=metric&appid="
    api_url += apiKey
    response = get(api_url)

    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        currLocation = str(x["name"])
        currTemperature = str(y["temp"])
        z = x["weather"]
        weatherDescription = str(z[0]["description"])
        spch = f"Its currently {currTemperature} degree celsius and {weatherDescription} in {currLocation}"
        speak(spch)
    else:
        speak("Sorry, Some error occurred")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your email", "your password")     #   Enter your email address and password to use the email functionality
    server.sendmail('your email', to, content)      #   Enter your email
    server.close()


def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        text = listener.listen(source)

    try:
        print("Recognizing...")
        query = listener.recognize_google(text, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak('Sorry, can you say that again please...')
        takeCommand()
        return "none"

    return query


if __name__ == "__main__":
    # takeCommand()
    wish()
    while True:
        query = takeCommand().lower()
        if 'exit' in query:
            speak("ok have a nice day!!")
            sys.exit()
        elif 'open command prompt' in query:
            speak("Ok opening Command Prompt")
            os.system("start cmd")
            exit()
        elif 'open visual studio code' in query:
            speak("Ok opening Visual studio Code")
            os.system("code")
            exit()
        # elif 'open camera' in query:
        #     speak("Ok opening camera")
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam', img)
        #         try:
        #             # print("Recognizing...")
        #             q = listener.recognize_google(text, language='en-in')
        #             q = q.lower()
        #             if 'exit' in q:
        #                 break
        #         except:
        #             pass
        #     cap.release()
        #     cv2.destroyAllWindows()
        #     exit()
        elif "current weather" in query:
            currWeather()
            exit() 
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results)
            exit()
        elif "open youtube" in query:
            speak("Ok opening youtube")
            webbrowser.open("youtube.com")
            exit()
        elif "open google" in query:
            speak("what should i search on google")
            srch = takeCommand().lower()
            speak("ok")
            webbrowser.open(f"{srch}")
            exit()
        elif ("message" in query) and ("send" in query):
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            speak("what message should i send")
            msg = takeCommand().lower()
            speak("ok sending message")
            kit.sendwhatmsg("+91xxxxxxxxxx",
                            msg, hour, minute) # Provide the number over here whom you want to send message
            exit()
        elif ("youtube" in query) and ("play" in query):
            speak("What should i play on youtube")
            song = takeCommand().lower()
            speak(f"Ok playing {song}")
            kit.playonyt(song)
            exit()
        elif "email" in query:
            try:
                speak("what should i send?")
                content = takeCommand().lower()
                to = 'receiver email'       # Provide the receiver's email over here
                sendEmail(to, content)
                speak(f"Email has been sent to {to}")
                exit()
            except Exception as e:
                print("sorry, currently iam not able to send the message")
                exit()
        else:
            speak("This is what I found on the web")
            webbrowser.open(f"{query}")
            exit()
    # speak("Do you have any other work?")
