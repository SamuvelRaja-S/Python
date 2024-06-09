import pyttsx3
txt=input("Enter the text :")
en=pyttsx3.init()
en.say(txt)
en.runAndWait()
