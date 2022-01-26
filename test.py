import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 50)
engine.setProperty("voice", "english")
engine.say("I am the text spoken after changing the speech rate.")
engine.runAndWait()
