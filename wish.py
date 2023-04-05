import datetime
from speak import speak
from takecommand import take_command
import speech_recognition as sr
from random import choice
import time


wishes = [
    "Would you like to know about today's weather condition?",
    "Would you like to hear some breaking news?",
    "Would you like to grab some funny jokes?",
    "Would you like to do some search on wikipedia?",
    "Would you like to set alarm for you?",
    "Do you have any queries to search on the internet?",
    "Would you like to know your current location?",
    "Would you like to know your ip address?",
    "Would you like to know your system's battery status?",
    "Would you like to know your internet speed?",
    "Sir, Want some music to be played?"
    ]
def wish():
    current_hour = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime('%H:%M %p')
    speak(f'Good morning sir, Its {current_time} now. Leo is online now.' if current_hour >= 0 and current_hour<12  else f'Good afternoon sir, Its {current_time}. Leo is online now.' if current_hour>12 and current_hour<18 else f'Good evening sir, Its {current_time}. Leo is online now.')
    time.sleep(1)
    def random_wish():
        question = choice(wishes)
        while True:
            speak(question)
            query = take_command()
            if 'no' in query or 'nope' in query or 'leave it' in query or 'dont say' in query or 'no thanks' in query or 'quit' in query or 'exit' in query or 'stop' in query:
                speak('Okay sir, Some other time.')
                break
            elif 'yes' in query or 'okay' in query or 'yep' in query or 'go on' in query or 'tell me' in query or 'tell' in query:
                if 'weather' in question:
                    from weatherforecast import weather_forecast
                    weather_forecast('dhangadhi')
                    break
                elif 'news' in question:
                    from news_headings import news_headings
                    news_headings()
                    break
                elif 'jokes' in question:
                    from jokes import random_jokes
                    random_jokes()
                    break
                elif 'wikipedia' in question:
                    from wikipediasearch import search_on_wikipedia
                    search_on_wikipedia(query=None)
                    break
                elif 'queries' in question:
                    from openai_leo import chatgpt_leo
                    chatgpt_leo(order=None)
                    break
                elif 'location' in question:
                    from findmylocation import find_location
                    find_location()
                    break
                elif 'ip address' in question:
                    from checkip import check_your_ip
                    check_your_ip()
                    break
                elif 'battery' in question:
                    from batterypercent import check_power
                    check_power()
                    break
                elif 'internet speed' in question:
                    from internetspeed import check_internet_speed
                    check_internet_speed()
                    break
                elif 'music' in question:
                    from youtubeplay import play_on_youtube
                    play_on_youtube()
                    break
            elif query == '':
                speak("Apology sir, I get no response from you.")
                break
    random_wish()
    time.sleep(1)
