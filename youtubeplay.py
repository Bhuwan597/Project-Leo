import pywhatkit as kit
from speak import speak
from takecommand import take_command
def play_on_youtube():
    count = 0
    while count <2:
        try:
            speak('Sir, What you want to play?')
            command = take_command()
            if command != '':
                kit.playonyt(command)
                break
            else:
                count+=1
                continue
        except:
            count+=1
