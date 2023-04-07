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
import os
import random
import cv2
import numpy as np
from PIL import Image

from PyQt5 import  QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from leogui import Ui_Leo
import playsound
query = ''
current_temperature = 'Dhangadhi (Temperature): 23° C'
location = 'Nepal'
def start():
    def find_temperature():
        global current_temperature
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
            sleep(3)
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
            sleep(8)
            while True:
                self.order = take_command()
                if 'wake up leo' in self.order or 'leo wake up' in self.order or 'lew' in self.order or 'helio' in self.order or 'wake up' in self.order or 'start' in self.order or 'online' in self.order or 'leo' in self.order:
                    main_function()
                    continue
                elif 'good bye' in self.order or 'good bye leo' in self.order or 'quit' in self.order or 'exit' in self.order or 'close' in self.order or 'bye' in self.order:
                    speak('Okay sir, I am leaving. Have a good day.')
                    sleep(0.4)
                    with open('reply.txt','a') as f:
                        f.truncate(0)
                    os.system(f"taskkill /im cmd.exe /f")
                    os.system(f"taskkill /im powershell.exe /f")
                else:
                    sleep(1)
                    continue

    startExecution = MainThread() 
    class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Leo()
            self.ui.setupUi(self)
            self.startTask()
            # self.ui.pushButton.clicked.connect(self.startTask)
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
            self.ui.movie = QtGui.QMovie('Leo GUI/recognizing.gif')
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie('Leo GUI/robot.gif')
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
            playsound.playsound('Leo GUI/welcomeback.mp3', False)
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



if len(os.listdir('samples')) == 0:
    address = 'http://192.168.1.68:4747/video'



    cam = cv2.VideoCapture(address)# Create a video capture object, helpful to create videos through webcam
    cam.set(3,1000) # Set video FrameWidth
    cam.set(4,1000) # Set video FrameHeight


    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # Hear cascade classifier is an effective object detection approach

    face_id = random.randint(0,9)

    speak('Sir, Please look at camera. I am taking your samples.')

    count = 0

    while True:

        ret,img = cam.read() # read frames using above crated object\
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert image to another color
        faces = detector.detectMultiScale(converted_image,1.3,5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2) # Used to draw rectangles of any image
            count+= 1


            cv2.imwrite('samples/face.'+ str(face_id) + '.' + str(count) + '.jpg', converted_image[y:y+h,x:x+w])
            # Captures and save image in dataset folder

            cv2.imshow('image', img) # Used to display image in window

        k = cv2.waitKey(100) & 0xff # Wait for a pressed key
        if k == 27:
            break
        elif count>=200: # Takes 200 samples
            break

    speak('Sample Taken, Now wait until I process your face prints.')
    cam.release()
    cv2.destroyAllWindows()


    path = 'samples' # Path for samples taken

    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Pattern Histograms
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


    def Images_And_Labels(path): # function to fetch the images and labels

        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []

        for imagePath in imagePaths: # to iterate particular image path

            gray_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_arr = np.array(gray_img,'uint8') #creating an array

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)

            for (x,y,w,h) in faces:
                faceSamples.append(img_arr[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    speak("Sir, wait for few seconds.")

    faces,ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')  # Save the trained model as trainer.yml

    speak('Your Face prints have been registered.')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadepath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadepath)



    font = cv2.FONT_HERSHEY_SIMPLEX

    no = 1
    names = ['','Bhuwan Acharya']
    address = 'http://192.168.1.68:4747/video'



    cam = cv2.VideoCapture(address)
    cam.set(3,1000)
    cam.set(4,1000)



    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)


    count =0
    while True:
        if count >= 3:
            break
        ret,img = cam.read()

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH))
        )
        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)

            id,accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

            if (accuracy < 70):
                id = names[no]
                print(id)
                accuracy = '{0}%'.format(round(100 - accuracy))
                cv2.putText(img, str(id), (x+5,y-5), font,1, (255,255,255),2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1, (255,255,0),1)
                playsound.playsound('Leo GUI/verificationsuccessful.wav', False)
                speak('Verification successfull.') 
                sleep(1)
                cam.release()
                cv2.destroyAllWindows()
                start()
            else:
                count+= 1
                accuracy = '{0}%'.format(round(100 - accuracy))
                cv2.putText(img, 'unknown', (x+5,y-5), font,1, (255,255,255),2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1, (255,255,0),1)
                playsound.playsound('Leo GUI/verificationfailed.wav', False)
                speak('Verification Failed.')
                sleep(1)
                print(id,accuracy)

        cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
else:


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadepath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadepath)



    font = cv2.FONT_HERSHEY_SIMPLEX

    no = 1
    names = ['','Bhuwan Acharya']



    # cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam = cv2.VideoCapture('http://192.168.1.68:4747/video')
    cam.set(3,1000)
    cam.set(4,1000)



    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)


    count =0
    while True:
        if count >= 3:
            break
        ret,img = cam.read()

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH))
        )
        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)

            id,accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

            if (accuracy < 70):
                id = names[no]
                print(id)
                accuracy = '{0}%'.format(round(100 - accuracy))
                cv2.putText(img, str(id), (x+5,y-5), font,1, (255,255,255),2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1, (255,255,0),1)
                playsound.playsound('Leo GUI/verificationsuccessful.wav', False)
                speak('Verification successfull.') 
                sleep(1)
                cam.release()
                cv2.destroyAllWindows()
                start()
            else:
                count+= 1
                accuracy = '{0}%'.format(round(100 - accuracy))
                cv2.putText(img, 'unknown', (x+5,y-5), font,1, (255,255,255),2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1, (255,255,0),1)
                playsound.playsound('Leo GUI/verificationfailed.wav', False)
                speak('Verification Failed.')
                sleep(1)
                print(id,accuracy)

        cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()