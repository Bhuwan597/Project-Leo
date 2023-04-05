from plyer import notification
from takecommand import take_command
from speak import speak
from time import sleep
import speech_recognition as sr
import threading
query = ''
def reminder():
    global query
    count = 0
    while count < 2:
        speak('What will be the purpose for this reminder?')
        message = take_command()
        speak('Sir, After how much minutes should I remind you?')
        time = float(input('\nType the minutes:\t'))
        if message!= '' and time!= '':
            speak(f'Reminder for {message} is set successfully.')
            sleep(60*time)
            notification.notify(title='Leo Reminder',message=message,timeout = 10, app_icon = 'bell.ico')
            speak(f'Sir, {message}')
            break
        else:
            count += 1
            speak('Sorry sir, I failed to set reminder for you. Try again, please.')
            continue