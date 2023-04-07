from email.message import EmailMessage
from takecommand import take_command
from speak import speak
import smtplib
from yaspin import yaspin
from yaspin.spinners import Spinners
import time
import tkinter as tk
import tkinter.font as tkFont

def send_email():
    count = 0
    with yaspin(Spinners.noise, text='Sending email ') as sp:
        while True:
            speak('Sir, Type the email address you want to send email.')
            sp.ok()
            root = tk.Tk()
            #setting title
            root.title("Email Address")
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
            GLabel_269["text"] = "Type the email address you want to send this email:"
            GLabel_269.place(x=40,y=30,width=440,height=58)
            root.mainloop()
            to = entry_value.get()
            sp.start()
            speak('What is the subject of your email, sir?')
            sp.ok()
            subject = take_command()
            sp.start()
            speak('Sir, what will be the content of your email message?')
            sp.ok()
            content = take_command()
            try:
                speak(f'You want to send email to, {to} with message of, {content} and with subject of, {subject}. Are you sure, you want to send this email? If yes then say, "send this email" or if no, you can say "dont send"')
                confirmation = take_command()
                if "don't send" in confirmation or 'no' in confirmation or 'no send' in confirmation or 'exit' in confirmation or 'quit' in confirmation or 'stop' in confirmation:
                    speak('Okay sir, I will not send this email.')
                    break
                elif 'send this email' in confirmation or 'yes' in confirmation or 'send email' in confirmation or 'send' in confirmation:
                    sp.start()
                    sp.spinner = Spinners.arc  # spinner type
                    sp.text = f"Sending Email to {to}"    # text along with spinner
                    sp.color = "green"         # spinner color
                    sp.side = "right"          # put spinner to the right
                    sp.reversal = True         # reverse spin direction
                    msg = EmailMessage()
                    msg['subject'] = subject
                    msg['From'] = 'v1acharya34@gmail.com'
                    msg['To'] = to
                    msg.set_content(content)
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login('v1acharya34@gmail.com','ogfirexfmdsdysng')
                    server.send_message(msg)
                    server.quit()
                    sp.ok()
                    speak(f'Email has been sent to {to}')
                    from desktop_notify import desktop_notify
                    desktop_notify('Email sent successfully', f'Email has been sent to {to}')
                    break
            except:
                sp.fail()
                count += 1
                if count >=2:
                    speak('Sorry sir, I continuously failed to send your email messages.')
                    break
                else:
                    speak('Pardon sir, I failed to send email this time. Would you please, try sending again?')
                continue

