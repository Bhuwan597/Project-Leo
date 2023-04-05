# from requests import get

# url = 'https://dms.licdn.com/playlist/C4E0DAQFc_rWjrF_7BA/learning-original-video-vbr-720/0/1619744711826?e=1680695592&v=beta&t=FodDEbZVEDGNV72LldD1VY6QoXYqoT7CygY-TXPOokc'
# chunk_size = 256

# r = get(url, stream=True)
# with open('Downloads/video.mp4','wb+') as f:
#     for chunk in r.iter_content():
#         f.write(chunk)

from pytube import YouTube
import tkinter as tk
import tkinter.font as tkFont
from speak import speak
import time
from yaspin import yaspin
from yaspin.spinners import Spinners
from desktop_notify import desktop_notify

def download_video():
    speak('Sir, please paste the link you want to download.')
    root = tk.Tk()
    #setting title
    root.title("Youtube Video Download")
    #setting window size
    width=500
    height=220
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    entry_value = tk.StringVar()
    GLineEdit_219=tk.Entry(root,textvariable=entry_value)
    GLineEdit_219["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_219["font"] = ft
    GLineEdit_219["fg"] = "#333333"
    GLineEdit_219["justify"] = "center"
    GLineEdit_219.place(x=100,y=90,width=286,height=48)
    def command():
        root.destroy()
    GButton_980=tk.Button(root)
    GButton_980["activebackground"] = "#5fb878"
    GButton_980["activeforeground"] = "#fbf5f5"
    GButton_980["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=14)
    GButton_980["font"] = ft
    GButton_980["fg"] = "#000000"
    GButton_980["justify"] = "center"
    GButton_980["text"] = "Ok"
    GButton_980.place(x=200,y=160,width=107,height=33)
    GButton_980["command"] = command
    GLabel_269=tk.Label(root)
    GLabel_269["activeforeground"] = "#5fb878"
    ft = tkFont.Font(family='Times',size=16)
    GLabel_269["font"] = ft
    GLabel_269["fg"] = "#333333"
    GLabel_269["justify"] = "center"
    GLabel_269["text"] = "Paste the link below:"
    GLabel_269.place(x=40,y=30,width=400,height=58)
    root.mainloop()
    url = entry_value.get()
    while True:
        try:
            with yaspin(Spinners.arc, text='Downloading Video') as sp:
                speak('Download on progress sir')
                yt_video = YouTube(url)
                video_resolutions = yt_video.streams.filter(progressive=True, res='720p').first()
                video_resolutions.download('C:\\Users\\v1ach\\OneDrive\\Desktop\\Project Leo\\downloads')
                sp.ok()
                speak('Video Downloaded successfully.')
                time.sleep(1)
                desktop_notify('Video Downloaded', f'{yt_video.title}')
                break
        except:
            sp.fail()
            speak('Sorry sir, I failed to download the video. Let me try again.')

        try:
            with yaspin(Spinners.arc, text='Downloading Video') as sp:
                speak('Download on progress sir')
                yt_video = YouTube(url)
                video_resolutions = yt_video.streams.filter(progressive=True, res='360p',).first()
                video_resolutions.download('C:\\Users\\v1ach\\OneDrive\\Desktop\\Project Leo\\downloads')
                sp.ok()
                speak('Video Downloaded successfully.')
                time.sleep(1)
                desktop_notify('Video Downloaded', f'{yt_video.title}')
                break
        except:
            sp.fail()
            speak('Sorry sir, I failed to download the video.')

        finally:
            break