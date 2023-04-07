# import os

# def open_system_apps(query):
#     root_dir = 'C:\\Users\\v1ach\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'
#     with open('commands/commandprompt.txt','r') as f:
#         for line in f.readlines():
#             if query in line:
#                 file_to_search = 'Command Prompt.lnk'
#                 for path,_,files in os.walk(root_dir):
#                     if file_to_search in files:
#                         full_path = os.path.join(root_dir,path,file_to_search)
#                         os.startfile(full_path)
#                         break
#                 break
#     with open('commands/fileexplorer.txt', 'r') as f:
#         for line in f.readlines():
#             if query in line:
#                 file_to_search = 'File Explorer.lnk'
#                 for path,_,files in os.walk(root_dir):
#                     if file_to_search in files:
#                         full_path = os.path.join(root_dir,path,file_to_search)
#                         os.startfile(full_path)
#                         break
#                 break      
#     with open('commands/fileexplorer.txt', 'r') as f:
#         for line in f.readlines():
#             if query in line:
#                 file_to_search = 'File Explorer.lnk'
#                 for path,_,files in os.walk(root_dir):
#                     if file_to_search in files:
#                         full_path = os.path.join(root_dir,path,file_to_search)
#                         os.startfile(full_path)
#                         break
#                 break      
          

# open_system_apps('Command')

# from pynput.keyboard import Key,Controller
# keyboard = Controller()
import pyautogui
import time
import os
 
# Running the aforementioned command and saving its output
# output = os.popen('wmic process get description, processid').read()
# print(output)
 
# Displaying the output
# process = 'calculatorapp'
# def task_killer(process):
#     try:
#         os.system(f"taskkill /im {process}.exe /f")
#         print('Successfully closed')
#     except:
#         print('Failed')

# task_killer(process)

# to_replace = ('aboard','about','above','across','after','against','along','amid','among','anti','around','as','at','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round','save','since','than','through','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without','a','an','the','search','open','launch','start','go to','hey','leo','please','hey')

# sentence = tuple((input('type the application name: ')).lower().split())
# new_sentence = ''

# for word in sentence:
#     if word not in to_replace:
#         new_sentence+= f'{word} '   

# pyautogui.press('win')
# pyautogui.write(new_sentence)
# time.sleep(0.5)
# pyautogui.press('enter')


# apps = {
#     'command prompt': 'cmd',
#     'paint': 'paint',
#     'word': 'winword',
#     'excel': 'excel',
#     'power point': 'powerpnt',
#     'vs code': 'code',
#     'visual studio code': 'code',
#     'powerpoint': 'powerpnt',
#     'edge': 'msedge',
#     'chrome': 'chrome',
#     'power shell': 'powershell',
#     'powershell': 'powershell',
#     'calculator': 'calculatorapp',
# }
# import pywhatkit as kit
# import webbrowser
# url = "https://docs.python.org/library/webbrowser.html"
# webbrowser.get(using='google-chrome').open(url,new=2)
# kit.search('google.com')
# webbrowser.open('youtube.com')
# webbrowser.open_new('youtube.com')
# webbrowser.open_new_tab('youtube.com')

# pyautogui.press('win')
# time.sleep(0.2)
# pyautogui.write('google chrome')
# pyautogui.press('enter')
# time.sleep(2)
# pyautogui.write('codewithharry.com')
# time.sleep(0.2)
# pyautogui.press('enter')

# os.system("taskkill /im Photo.UI.exe /f")

# kit.sendwhatmsg_instantly('+9779821669048','Hi Bhwan',tab_close=True)
# time.sleep(1)
# pyautogui.press('enter')

 
# import openai
# openai.api_key = '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'
# model_name = 'text-davinci-003'
# completion = openai.Completion.create(
#                     model = model_name,
#                     prompt = 'Mahendra singh dhoni',
#                     max_tokens = 1024,
#                     n=1,
#                     stop = None
# )
# response = completion.choices[0].text
# print(response)

# from requests import get
# from bs4 import BeautifulSoup
# import random
# types = ['nation', 'sports','science-and-technology']
# all_news = []
# for item in types:
#     url = f'https://www.nepalnews.com/s/{item}'
#     r = get(url).text
#     soup = BeautifulSoup(r,'html.parser')
#     content = soup.find_all('div', class_ = 'el-content uk-panel uk-margin-small-top st-list-intro')
#     for news in content:
#         all_news.append(news.text)

# random_10_news = random.sample(all_news, 10)
# for news in random_10_news:
#     print(news)

# from speak import speak
# with open('gmail.txt', 'r+') as f:
#     import datetime
#     crnt_date = datetime.datetime.now().strftime('%Y/%m/%d')
#     crnt_time = datetime.datetime.now().strftime('%H:%M:%S %p')
#     if os.stat('gmail.txt').st_size == 0:
#         speak('Wait sir, I need to configure your email address and password once.')
#         speak('Type your email address, sir.')
#         email_address = input('Email Address:\t')
#         speak('Type your email password, sir.')
#         email_password = input('Password:\t')
#         f.write(f"{email_address}\n{email_password}")
#     else:
#         gmail_info = f.readlines()
#         email_address = gmail_info[0]
#         email_password = gmail_info[1]
#         from email.message import EmailMessage
#         import smtplib
#         server = smtplib.SMTP('smtp.gmail.com',587)
#         server.ehlo()
#         server.starttls()
#         server.login(email_address,email_password)
# importing requests and json
# import requests
# from math import floor
# # base URL
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# # City Name 
# CITY = "Dhangadhi"
# # API key 
# API_KEY = "612c6faed68e1d51d4ca0809cc1c96ef"
# # upadting the URL
# URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# # HTTP request
# response = requests.get(URL)
# # checking the status code of the request
# if response.status_code == 200:
#    data = response.json()
#    temperature = floor(data['main']['temp'] -273.15)
#    weather = data['weather'][0].get('description')
#    humidity = data['main']['humidity']
#    wind_speed = data['wind']['speed']
#    print(temperature,weather,humidity, wind_speed)

# else:
#    # showing the error message
#    print("Error in the HTTP request")

# os.system('shutdown -s -f -t 04')

# import ffmpeg
# import pytube
# link = 'https://youtu.be/xSaP3QpwWmY'
# yt = pytube.YouTube(link)
# filename = yt.title
# yt.streams.filter(res="720p", progressive=True).first().download()


# from takecommand import take_command


# query = take_command()

# splitted_words = query.split()

# digit = 0
# for i in splitted_words:
#     if i.isdigit():
#         digit = int(i)

# if 'minutes' in query or 'minute' in query:
#     sleeping_time = digit*60
# if 'hour' in query or 'hours' in query:
#     sleeping_time = digit*60*60
# if 'day' in query or 'days' in query:
#     sleeping_time = digit*60*60*24

# print(sleeping_time)
# os.system("TASKKILL /F /IM Microsoft.Photos.exe")

# import cv2
# import requests
# import numpy as np

# url = 'http://192.168.1.68:8080/shot.jpg'

# while True:
#     r = requests.get(url)
#     img_array = np.array(bytearray(r.content),dtype=np.uint8)
#     img = cv2.imdecode(img_array,-1)
#     cv2.imshow('Camera', img)
#     if cv2.waitKey(1) &0xff == 27:
#         break

# cv2.destroyAllWindows()

#!/usr/bin/env python3

import cv2

cap = cv2.VideoCapture('http://192.168.1.68:4747/video')

while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    cv2.waitKey(1)