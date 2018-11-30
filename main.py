#Python Voice Search AI BOT
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import win32com.client as wincl
import webbrowser
import requests as req

speak2 = wincl.Dispatch("SAPI.SpVoice")

 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
  
    r = sr.Recognizer()
    print("\n Sir, seems like we have a trouble with ur car")
    with sr.Microphone() as source:
        print("How may i help u Sir .Please Say something!")
        audio = r.listen(source)
 
   
    data = ""
  
   
 try:
      
        data = r.recognize_google(audio)
        print("Sir u requested for : " + data)
    except sr.UnknownValueError:
        print("Bond Bot Speech Recognition could not understand audio,please say again")
    except sr.RequestError as e:
        print("Could not request results from  service; {0},Please say again ".format(e))
 
    return data
 
def cordax(data):
    
    if "help" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, dont panic , we are sending u help ")
        speak2.Speak("Hold on Sir, dont panic , we are sending u help , take emergency needing and ur location has been marked and live track of ur cell phone is under way.Bond bot will rescue u ")
        webbrowser.open("http://poster.keepcalmandposters.com/4344569.jpg")
    if "Google" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will open Google for you")
        speak2.Speak("Hold on Sir, I will open Google for you")
        webbrowser.open("https://www.google.com")

    if "YouTube" in data:
        speak("Hold on Sir, I will open YouTube for you")
        speak2.Speak("Hold on Sir, I will open YouTube for you")
        webbrowser.open("https://www.youtube.com")

    


    if "Twitter" in data:
        speak("Hold on Sir, I will open Twitter for you")
        speak2.Speak("Hold on Sir, I will open Twitter for you")
        webbrowser.open("https://www.twitter.com")

    
    if "Facebook" in data:
        speak("Hold on Sir, I will open Facebook for you")
        speak2.Speak("Hold on Sir, I will open Facebook for you")
        webbrowser.open("https://www.facebook.com")


    if "search for" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will search for " + location + ".")
        speak2.Speak("Hold on Sir, I will search for " + location + ".")
        webbrowser.open("https://www.google.com/search?q=" + location + "")

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        speak2.Speak("Hold on Sir, I will search for " + location + ".")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(2)
speak("Sir seems like we have a trouble with ur car")
speak2.Speak("Hello Sir seems like we have a trouble with ur car, we have notified the nearest service center, u can also search for nearest service  center manully in the mean time u can search anything like google or youtube or search for or where is in the pass time" )
while 1:
    data = recordAudio()
    cordax(data)
