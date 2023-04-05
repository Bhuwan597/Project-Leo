from speak import speak
import pywhatkit as kit
import time
import tkinter as tk
import tkinter.font  as tkFont
# from pynput.keyboard import Key,Controller 
from takecommand import take_command
import pyautogui
from yaspin.spinners import Spinners
from yaspin import yaspin
def send_whatsapp_messages():
    with yaspin(Spinners.noise, text='Sending whatsapp message  ') as sp:
        speak('\nType the number you want to send message')
        sp.ok()
        root = tk.Tk()
        #setting title
        root.title("Whatsapp Number")
        #setting window size
        width=484
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
        GLabel_269["text"] = "Type the number you want to send the message:"
        GLabel_269.place(x=40,y=30,width=409,height=58)
        root.mainloop()
        number = '+977'+ entry_value.get()
        sp.start()
        speak('\nWhat message would you like to send?')
        count = 0
        while True:
            sp.ok()
            message = take_command().lower()
            sp.start()
            sp.spinner = Spinners.arc  # spinner type
            sp.text = f"Sending message to {number}"    # text along with spinner
            sp.color = "green"         # spinner color
            sp.side = "right"          # put spinner to the right
            sp.reversal = True         # reverse spin direction
            if message != '':
                try:
                    kit.sendwhatmsg_instantly(number,message,tab_close=True)
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)
                    speak(f"Message sent to {number}!")
                    from desktop_notify import desktop_notify
                    desktop_notify('Whatsapp Message',f"Message sent to {number}!")
                    break
                except:
                    count+=1
                    if count>=2:
                        speak('\nSorry sir, Some error occured while sending your message.')
                        break
                    continue
            else:
                count+=1
                if count>=2:
                    speak('\nSorry sir, Some error occured while sending your message.')
                    break
                else:
                    speak('\nTry saying the message again')
                continue