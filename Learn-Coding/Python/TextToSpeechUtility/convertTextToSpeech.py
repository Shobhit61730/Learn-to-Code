'''
To convert text to speech, we need library : pyttsx3
Use pip install pyttsx3 to install required library.
'''
import pyttsx3
  
# initialisation
engine = pyttsx3.init(driverName = "sapi5", debug = False)

engine.say("Hello World")
engine.say("This is my Hacktober Contribution")
engine.runAndWait()