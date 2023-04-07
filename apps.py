import pyautogui
from time import sleep
from speak import speak
import os
from takecommand import take_command
import webbrowser
import pywhatkit as kit
def open_apps(query):
    to_replace = ('open','start','launch','go to', 'navigate','search')
    app_name = ''
    for item in query.split():
        if item not in to_replace:
            app_name+= f'{item} '
    if 'chrome' in app_name or 'google chrome' in app_name:
        print(app_name, query)
        count = 0
        while True:
            if count >=2:
                break
            speak('Sir, what do you want to search on chrome browser?')
            website_name = take_command()
            shorlisted_query = ''
            for word in website_name.split():
                if word not in to_replace:
                    shorlisted_query+= word
            if website_name != '':
                pyautogui.press('win')
                sleep(1)
                pyautogui.write('google chrome')
                sleep(0.5)
                pyautogui.press('enter')
                sleep(3)
                pyautogui.write(shorlisted_query)
                sleep(1)
                pyautogui.press('enter')
                break
            else:
                count+=1
                speak('Say that again please?')
    elif 'edge' in app_name or 'microsoft edge' in app_name:
        count = 0
        while True:
            if count >=2:
                break
            speak('Sir, what do you want to search on edge browser?')
            website_name = take_command()
            shorlisted_query = ''
            for word in website_name.split():
                if word not in to_replace:
                    shorlisted_query+= word
            if website_name != '':
                pyautogui.press('win')
                sleep(1)
                pyautogui.write('edge')
                sleep(0.5)
                pyautogui.press('enter')
                sleep(3)
                pyautogui.write(shorlisted_query)
                sleep(1)
                pyautogui.press('enter')
                break
            else:
                count+=1
                speak('Say that again please?')
    elif 'music' in app_name or 'songs' in app_name or 'song' in app_name:
        from youtubeplay import play_on_youtube
        play_on_youtube()
    else:
        pyautogui.press('win')
        sleep(1)
        pyautogui.write(app_name)
        sleep(1)
        pyautogui.press('enter')
        speak(f'Successfully opened {app_name}')
        
def close_apps(query):
    to_replace = ('quit','exit','stop','close','browser')
    app_name = ''
    for item in query.split():
        if item not in to_replace:
            app_name+= f'{item}'
    apps = {
    'commandprompt': 'cmd',
    'paint': 'paint',
    'word': 'winword',
    'excel': 'excel',
    'powerpoint': 'powerpnt',
    'vscode': 'code',
    'visualstudiocode': 'code',
    'powerpoint': 'powerpnt',
    'edge': 'msedge',
    'microsoftedge': 'msedge',
    'microsoftage': 'msedge',
    'age': 'msedge',
    'chrome': 'chrome',
    'googlechrome': 'chrome',
    'powershell': 'powershell',
    'powercell': 'powershell',
    'powersale': 'powershell',
    'calculator': 'calculatorapp',
    'notepad' : 'notepad',
    'music':'runtimebroker',
    'mediaplayer':'runtimebroker',
    'musicplayer':'runtimebroker',
    'player':'runtimebroker',
    }
    if app_name!= '':
        for key,value in apps.items():
            if app_name in key or app_name in value:
                process = apps[app_name]
                try:
                    os.system(f"taskkill /im {process}.exe /f")
                    speak(f'Successfully closed {app_name}')
                    break
                except Exception as e:
                    speak(f'Sorry sir, Failed to close {app_name}')
                    break