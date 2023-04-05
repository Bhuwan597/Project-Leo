from main import main_function
from takecommand import take_command
from time import sleep
from speak import speak
import speech_recognition as sr
import sys
import requests
import psutil
# from bs4 import BeautifulSoup
from math import floor

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from leogui import Ui_Leo
query = ''
current_temperature = 'Dhangadhi (Temperature): 23° C'
location = 'Nepal'
def find_temperature():
    global current_temperature
    speak('Wait sir, I am collecting some information before coming online.')
    try:
        ip_address = requests.get('https://api.ipify.org').text
        url='https://get.geojs.io/v1/ip/geo/'+ ip_address + '.json'
        geo_array = requests.get(url).json()
        city = geo_array['city']
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name 
        CITY = city
        # API key 
        API_KEY = "612c6faed68e1d51d4ca0809cc1c96ef"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        data = response.json()
        temperature = floor(data['main']['temp'] -273.15)
        current_temperature = f'{city} (Temperature): {temperature}° C'
        with open('reply.txt','a') as f:
            f.truncate(0)
    except:
        pass

find_temperature()
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
    
    def TaskExecution(self):
        import winsound
        winsound.Beep(700, 400)
        while True:
            self.order = take_command()
            if 'wake up leo' in self.order or 'leo wake up' in self.order or 'lew' in self.order or 'helio' in self.order or 'wake up' in self.order or 'start' in self.order or 'online' in self.order:
                main_function()
                continue
            elif 'good bye' in self.order or 'good bye leo' in self.order or 'quit' in self.order or 'exit' in self.order or 'close' in self.order or 'bye' in self.order:
                speak('Okay sir, I am leaving. Have a good day.')
                sleep(0.4)
                with open('reply.txt','a') as f:
                    f.truncate(0)
                sys.exit()
            else:
                sleep(1)
                continue

startExecution = MainThread() 
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Leo()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.closeTask)
        self.showMaximized()
        global location
        try:
            ip_address = requests.get('https://api.ipify.org').text
            url='https://get.geojs.io/v1/ip/geo/'+ ip_address + '.json'
            geo_array = requests.get(url).json()
            sleep(0.4)
            city = geo_array['city']
            country = geo_array['country']
            country_code = geo_array['country_code']
            location = f'{country} ({country_code}) , {city}'
        except:
            pass

    def startTask(self):
        self.ui.movie = QtGui.QMovie('Leo GUI/fxVE.gif')
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie('Leo GUI/MImN.gif')
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie('Leo GUI/loading.gif')
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie('Leo GUI/J4o.gif')
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showInfo)
        timer.start(1000)
        startExecution.start()
    def closeTask(self):
        with open('reply.txt','a') as f:
            f.truncate(0)
        self.close()
    def showInfo(self):
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S %p')
        current_date = datetime.now().strftime('%Y/%m/%d')
        self.ui.textBrowser.setText(current_date)
        self.ui.textBrowser_2.setText(current_time)
        self.ui.textBrowser_4.setText(current_temperature)
        battery_percentage = psutil.sensors_battery().percent
        self.ui.progressBar.setValue(battery_percentage)
        self.ui.textBrowser_5.setText(f'{battery_percentage}%')
        self.ui.textBrowser_3.setText(location)
        with open('reply.txt', 'r') as f:
            text = f.readline()
            self.ui.textEdit.setText(text)

app = QApplication(sys.argv)
leo = Main()
leo.show()
exit(app.exec_())
