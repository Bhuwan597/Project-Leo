import pyjokes
from speak import speak
from takecommand import take_command
from time import sleep
def random_jokes():
    while True:
        try:
            joke = pyjokes.get_joke()
            speak('Okay sir, Joke seems to be like this: ')
            speak(joke)
            sleep(1)
            speak('Do you want some more funny jokes?')
            query = take_command()
            if 'yes' in query or 'okay' in query or 'yep' in query or 'go on' in query or 'tell me' in query or 'tell' in query:
                continue
            elif 'no' in query or 'nope' in query or 'stop' in query:
                speak('Okay sir, Some other time.')
                sleep(1)
                break
            else:
                break
        except:
            speak('Apology sir, There was an error in fetching jokes.')
            break