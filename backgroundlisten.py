import speech_recognition as sr
import time
import threading
import sys

query = ''
def background_listen(func):
    def callback(recognizer,audio):
        try:
            global query
            query = recognizer.recognize_google(audio)
        except:
            return ''
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    stop_listening = recognizer.listen_in_background(mic, callback)

    func(query)

    stop_listening()

