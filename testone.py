import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import google
import gmail
import webbrowser
import os
import smtplib

engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')

#for i in range(0,100):
 #   print(voices[i].id,i)
  #  if (voices[i].id == 'hindi'):
   #     break
engine.setProperty('voice',voices[10].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afernoon")
    else:
        speak("good evening")

    speak("i am your dad, yeah")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        #r.energy_threshold=100
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_bing(audio,language='en-in')
        print("user said ",query)
    except Exception as e:
        print(e)

        print("say that again please")
        return None

    return query


def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("hellwarrior007@gmail.com","hellwarrior")
    server.sendmail("hellwarrior007@gmail.com",to,content)
    server.close()


if __name__=="__main__":
    #speak("vineet is awesome")
    greet()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipeda..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'the time' in query:
            timestr=datetime.datetime.now().timestr("%H%M%S")
            speak(f"the time is {timestr}")
        

        elif "send emai" in query:
            try:
                speak("body please ?")
                content=takecommand()
                tp = 'sineetsingh@gmail.com'
                sendEmail(to,content)
                speak("email send")
            except Exception as e1:
                print(e1)
                speak("email not send")
s