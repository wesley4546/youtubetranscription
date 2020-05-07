import speech_recognition as sr

r = sr.Recognizer()

path = "audio.wav"

with sr.AudioFile(path) as source:
    audio = r.record(source)

    print(r.recognize_google(audio))