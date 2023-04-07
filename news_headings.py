from bs4 import BeautifulSoup
import requests
import time
from speak import speak
import speech_recognition as sr
import sys
import random

query = ''
def news_headings():
    global query
    '''This function takes no arguments. It simpy returns the latest national news in english language. It uses bs4 and requests module to scrape the news of nepalisansar.com. It returns empty string if it unable to fetch news'''

    def callback(recognizer,audio):
        try: 
            global query
            query =  recognizer.recognize_google(audio)
            if 'exit' in query:
                raise ValueError()
        except:
            pass
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    stop_listening = recognizer.listen_in_background(mic, callback)
    types = ['nation', 'sports','science-and-technology']
    all_news = []
    try:
        for item in types:
            url = f'https://www.nepalnews.com/s/{item}'
            r = requests.get(url).text
            soup = BeautifulSoup(r,'html.parser')
            content = soup.find_all('div', class_ = 'el-content uk-panel uk-margin-small-top st-list-intro')
            for news in content:
                all_news.append(news.text)
        random_10_news = random.sample(all_news, 10)
        for news in random_10_news:
            if 'exit' in query or 'quit' in query or 'stop' in query:
                speak('Okay sir, I will stop.')
                return
            elif 'repeat' in query or 'once more' in query or ' say again' in query:
                query = ''
                return news_headings()     
            speak(news)       
            time.sleep(0.5)
    except:
        speak('Sorry sir, I was unable to fetch news for you')
    stop_listening()