from plyer import notification
from takecommand import take_command
from speak import speak
from time import sleep
query = ''
def reminder():
    global query
    count = 0
    while count < 2:
        speak('What will be the purpose for this reminder?')
        message = take_command()
        speak('Sir, After how much time should I remind you?')
        query = take_command()
        splitted_words = query.split()
        digit = 0
        for i in splitted_words:
            if i.isdigit():
                digit = int(i)
                break
        sleeping_time=0
        if 'minutes' in query or 'minute' in query:
            sleeping_time = digit*60
        if 'hour' in query or 'hours' in query:
            sleeping_time = digit*60*60
        if 'day' in query or 'days' in query:
            sleeping_time = digit*60*60*24
        if message!= '' and sleeping_time!= '':
            speak(f'Reminder for {message} is set successfully.')
            def reminder_background():
                sleep(sleeping_time)
                notification.notify(title='Leo Reminder',message=message,timeout = 10, app_icon = 'bell.ico')
                speak(f'Sir, {message}')
            import threading
            threading.Thread(target=reminder_background).start()
            break
        else:
            count += 1
            speak('Sorry sir, I failed to set reminder for you. Try again, please.')
            continue