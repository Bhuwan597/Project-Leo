from speak import speak
import datetime
import time
import tkinter as tk
import tkinter.font as tkFont



def start_alarm():
    speak('Please, provide the time you want to set alarm')
    def playbeep():
           import winsound 
           winsound.Beep(700,2000)
    from yaspin import yaspin
    from yaspin.spinners import Spinners
    with yaspin(Spinners.noise, text='Setting alarm for you ') as sp:
        try:
            sp.ok()
            root = tk.Tk()
            #setting title
            root.title("Alarm")
            #setting window size
            width=560
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
            GLabel_269["text"] = "Type the time for alarm in format of day/hour/minutes"
            GLabel_269.place(x=40,y=30,width=480,height=58)
            root.mainloop()
            day,hour,min = entry_value.get().split('/')
            sp.start()
            sp.spinner = Spinners.arc  # spinner type
            sp.text = "Alarm Set"    # text along with spinner
            sp.color = "green"         # spinner color
            sp.side = "right"          # put spinner to the right
            sp.reversal = True         # reverse spin direction
            day_from_now = int(day) - int(datetime.datetime.now().day)
            d = int(day_from_now)+ (int(hour)-int(datetime.datetime.now().hour))/24 + (int(min) - int(datetime.datetime.now().strftime('%M')))/(24*60)
            alarm = datetime.timedelta(days=d)
            full_time = datetime.datetime.now() + alarm
            compare_alarm_time = full_time.strftime('%d/%H/%M')
            time.sleep(1)
            sp.ok()
            speak('Alarm Set successfully')
            def check_time_background():
                while True:
                    minute_left = (full_time.timestamp() - datetime.datetime.now().timestamp())//60
                    if str(compare_alarm_time) == datetime.datetime.now().strftime('%d/%H/%M'):
                        count = 0
                        from desktop_notify import desktop_notify
                        desktop_notify('Alarm', f'Wake up Bhuwan its {compare_alarm_time}' )
                        while True:
                            speak('Wake up Bhuwan')
                            count+=1
                            if count == 6:
                                break
                            playbeep()
                            time.sleep(1)
                        break
                    else:
                        # speak(f'{int(minute_left)} minutes left for alarm')
                        time.sleep(60 - int(datetime.datetime.now().strftime('%S')))
            import threading
            threading.Thread(target=check_time_background).start()
        except Exception as e:
            sp.fail()
            time.sleep(1)
            speak('Sorry something went wrong while setting up alarm')