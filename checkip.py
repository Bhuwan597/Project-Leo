from requests import get
from yaspin import yaspin
from yaspin.spinners import Spinners
from speak import speak
from time import sleep
def check_your_ip():
    speak('Hang in there for few seconds until i find your ip address.')
    count = 0
    while True:
        with yaspin(Spinners.noise, text='Locating your ip') as sp:
            try:
                ip = get('https://api.ipify.org').text
                from desktop_notify import desktop_notify
                sp.spinner = Spinners.arc  # spinner type
                sp.color = "green"         # spinner color
                sp.side = "right"          # put spinner to the right
                sp.reversal = True         # reverse spin direction
                speak(f"Your ip address is {ip}")
                sleep(0.5)
                desktop_notify('Ip Address', f"Your ip address is {ip}")
                sp.ok()
                break
            except:
                count+=1
                if count>=2:
                    speak('Some error occured while finding your ip address.')
                    break
                else:
                    speak('Let me try again sir.')
                    sp.fail()
                    continue
        