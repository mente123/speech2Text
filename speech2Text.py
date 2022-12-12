from re import S

from itsdangerous import exc
import pysttx3
import speech_recognition as sr

def get():
    voice = sr.Recognizer()
    with sr.Microphone as source: # record a voice using a microphone
        print("Say something, please: ")
        audio = voice.listen(source)
        print("done")
        
        try:
            text = voice.recognize_google(audio)  # convert the voice into text using google speech recognition
            print("you have said", text)
        except Exception as e:
            print(e)
        
get()