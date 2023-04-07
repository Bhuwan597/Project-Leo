from sys import exit
# Function import
from wish import wish
from takecommand import take_command
from time import sleep
from speak import speak
import os
import playsound


def background_compute():
    playsound.playsound('Leo GUI/background.wav', False)


to_replace = ('aboard','about','above','across','after','against','along','amid','among','anti','around','as','at','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round','save','since','than','through','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without','a','an','the','hey','leo','please','hey','wake up','hello','me','helio','lew','what','where','when','who','how','which','is','am','are','now')

def main_function():
    wish()
    count = 0
    while count<=3:
        if count == 3:
            speak('Sorry sir, I hear not any commands from you. So i am going offline now, you can call me any time.')
            break
        sleep(1)
        # speak('Tell me sir if something else i can do for you?')
        query = take_command().split()
        if query != []:
            command = ''
            for word in query:
                if word not in to_replace:
                    command += f'{word} '
            count = 0
            if 'sleep' in command or 'stop' in command or 'nothing' in command or "don't have" in command or 'go offline' in command:
                speak('Okay sir, i am going offline now, you can call me any time.')
                background_compute()
                break
            elif 'exit' in command or 'quit' in command or 'good bye' in command or 'goodbye'in command  or 'good value' in command :
                speak('Okay sir, I am leaving. Have a good day.')
                background_compute()
                sleep(0.4)
                with open('reply.txt','a') as f:
                    f.truncate(0)
                os.system(f"taskkill /im cmd.exe /f")
                os.system(f"taskkill /im powershell.exe /f")
                exit()
            elif 'shutdown' in command or 'turn off' in command or 'shut down' in command:
                background_compute()
                speak('Okay sir, System will shut down in, 5')
                sleep(0.5)
                speak('4')
                sleep(0.5)
                speak('3')
                sleep(0.5)
                speak('2')
                sleep(0.5)
                speak('1')
                with open('reply.txt','a') as f:
                    f.truncate(0)
                os.system('shutdown -s -f -t 00')
            elif 'restart' in command or 're start' in command:
                background_compute()
                speak('Okay sir, System will restart on in, 5')
                sleep(0.5)
                speak('4')
                sleep(0.5)
                speak('3')
                sleep(0.5)
                speak('2')
                sleep(0.5)
                speak('1')
                with open('reply.txt','a') as f:
                    f.truncate(0)
                os.system('shutdown -r -f -t 00')               
            elif command.startswith(('open','start','launch','go to','navigate')):
                background_compute()
                from apps import open_apps
                open_apps(command)
                continue
            elif command.startswith(('close')):
                background_compute()
                from apps import close_apps
                close_apps(command)
                continue

            elif 'weather' in command or 'temperature' in command or 'forecast' in command:
                background_compute()
                from weatherforecast import weather_forecast
                weather_forecast('dhangadhi')
                continue
                
            elif 'jokes' in command or 'joke' in command or 'funny joke' in command:
                background_compute()
                from jokes import random_jokes
                random_jokes()
                continue
                
            elif 'news' in command or 'samachar' in command or 'headlines' in command or 'khabar' in command:
                background_compute()
                from news_headings import news_headings
                news_headings()
                continue
            elif 'battery percentage' in command or 'battery percent' in command or 'battery' in command:
                background_compute()
                from batterypercent import check_power
                check_power()
                continue 
            elif command.startswith('search') and 'wikipedia' in command:
                background_compute()
                from wikipediasearch import search_on_wikipedia
                search_on_wikipedia(query=command)
                continue 
            elif (command.startswith(('set')) and 'alarm' in command) or 'alarm' in command:
                background_compute()
                from startalarm import start_alarm
                start_alarm()
                continue
            elif (command.startswith(('set')) and 'reminder' in command) or 'reminder' in command:
                background_compute()
                from remind_me import reminder
                reminder()
                continue
            elif 'send email' in command or 'send gmail' in command or 'type email' in command or 'type gmail' in command:
                background_compute()
                from emailsend import send_email
                send_email()
                continue
            elif 'send whatsapp message' in command or 'send whatsapp' in command or 'whatsapp' in command:
                background_compute()
                from sendwhatsappmessages import send_whatsapp_messages
                send_whatsapp_messages()
                continue
            elif 'speed test' in command or 'wifi speed' in command or 'latency' in command or 'internet speed' in command or 'wifi signal' in command or 'wi-fi speed' in command:
                background_compute()
                from internetspeed import check_internet_speed
                check_internet_speed()
                continue
            elif 'my location' in command or 'current location' in command or 'location' in command:
                background_compute()
                from findmylocation import find_location
                find_location()
                continue
            elif 'ip address' in command:
                background_compute()
                from checkip import check_your_ip
                check_your_ip()
                continue
            elif 'play music' in command or 'play some music' in command or 'play songs' in command or 'play song' in command or 'listen music' in command or 'listen songs' in command:
                background_compute()
                from youtubeplay import play_on_youtube
                play_on_youtube()
                continue
            elif 'download video' in command or 'download youtube video' in command or 'download song' in command or 'youtube video' in command or 'download youtube song' in command or 'download youtube songs' in command:
                background_compute()
                from youtubevideodownloader import download_video
                download_video()
            elif 'screenshot' in command or 'screen shot' in command or 'capture screen' in command or 'capture the screen' in command:
                background_compute()
                from takescreenshot import take_screenshot
                take_screenshot()
                continue
            elif len(command.split()) > 4:
                background_compute()
                from openai_leo import chatgpt_leo
                chatgpt_leo(order=command)
                continue
            else:
                count+=1
                speak('I am sorry sir, Could you please say that again?')
        else:
            count+=1
            sleep(1)
            if count == 1:
                speak('How may i help you, sir?') 
            elif count == 2:
                speak('Sir, is there anything you would like me to do?')
            continue
    