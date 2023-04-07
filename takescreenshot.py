from PIL import Image
def take_screenshot():
    import pyautogui
    import random
    import time
    import os
    from speak import speak
    from takecommand import take_command
    from PIL import Image
    im = pyautogui.screenshot()
    time.sleep(1)
    filenames = str(random.randint(0,9)) + str(random.randint(0,9))+str(random.randint(0,9))
    im.save(r"C:\\Users\\v1ach\\OneDrive\\Pictures\\Screenshots\\"+"ss"+filenames+".jpg")
    speak('Sreenshot saved, Would you like to view it sir?')
    yes_no = take_command()
    if 'yes' in yes_no or 'okay' in yes_no or 'yeah' in yes_no or 'ok' in yes_no or 'sure' in yes_no or 'open' in yes_no or 'show' in yes_no:
        speak('Okay sir, I will open it for you.')
        os.startfile(r"C:\\Users\\v1ach\\OneDrive\\Pictures\\Screenshots\\"+"ss"+filenames+".jpg")
        time.sleep(1)
        while True:
            close_or_not = take_command()
            if 'exit' in close_or_not or 'quit' in close_or_not or 'close' in close_or_not:
                speak('Fine sir, Closing screenshot image.')
                os.system("TASKKILL /F /IM Microsoft.Photos.exe")
                break
            continue
    if 'no' in yes_no or "don't show" in yes_no or "don't" in yes_no or 'do not' in yes_no or 'exit' in yes_no or 'quit' in yes_no or 'close' in yes_no:
        speak('Okay, fine sir.')
    else:
        pass

