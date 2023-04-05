from yaspin import yaspin
from yaspin.spinners import Spinners
import time
with yaspin(Spinners.noise, text='Listening to your voice') as sp:
    for i in range(100):
        time.sleep(3)
        sp.ok()
        yes = input('Enter your name:')
        sp.start()
        print('\n')
        print(i)
        time.sleep(2)
