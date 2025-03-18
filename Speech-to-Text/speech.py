import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Saravana")
    audio=r.listen(source)

try:
    text=r.recognize_google(audio)
    print("You said:"+text)
except sr.UnknownValueError:
    print("Google speech recognition code coudnt understand audio")
except sr.RequestError as e:
    print("Couldnt understand".format(e))
