from pyttsx3 import Engine


def speak(audio:str):
    '''Takes argument audio as a string and pyytsx3 engine speaks it. It prints the audio before speaking - Developed by Bhuwan Acharya.'''
    engine = Engine()
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voices', voices[0].id)
    with open('reply.txt', 'a+' ) as f:
        f.truncate(0)
        print(audio)
        engine.say(audio)
        f.write(f'{audio}\n')
        engine.runAndWait()
