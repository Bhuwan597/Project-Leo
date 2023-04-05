import speech_recognition as sr
from yaspin import yaspin
from yaspin.spinners import Spinners
from csv import DictWriter
import os
def take_command():
    '''This take command function takes no argument. It listen to your voice and r by using r_google function of speech_recognition module. It returns a valid lowecase string if it rs your voice else returns a empty string - Developed by Bhuwan Acharya.'''
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        try:
            with yaspin(Spinners.noise, text='Listening to your voice') as sp:
                recognizer.pause_threshold = 1
                # print('********* Listening *********')
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                sp.spinner = Spinners.arc  # spinner type
                sp.text = "Recognizing your voice"    # text along with spinner
                sp.color = "green"         # spinner color
                sp.side = "right"          # put spinner to the right
                sp.reversal = True         # reverse spin direction
                # print('********* Recognizing ********')
                say = recognizer.recognize_google(audio, language='en-in').lower()
                def append_query():
                    import datetime
                    crnt_date = datetime.datetime.now().strftime('%Y/%m/%d')
                    crnt_time = datetime.datetime.now().strftime('%H:%M:%S %p')
                    with open('commands.csv', 'a',newline='') as f:
                        csv_writer = DictWriter(f, fieldnames=['query','date','time'])
                        if os.stat('commands.csv').st_size == 0:
                            csv_writer.writeheader()
                        csv_writer.writerows([{
                            'query':say,
                            'date': crnt_date,
                            'time': crnt_time,
                        }])
                append_query()
                print(f'\nYou said: {say}')
                return say
        except:
            return ''
        