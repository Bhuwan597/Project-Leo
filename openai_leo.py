from speak import speak
from yaspin import yaspin
from yaspin.spinners import Spinners
import speech_recognition as sr
import sys
query = ''
def chatgpt_leo(order = None):
    with yaspin(Spinners.noise, text='Searching your query') as sp:
        if order != None:
            try:
                import openai
                openai.api_key = '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'
                model_name = 'text-davinci-003'
                sp.ok()
                sp.spinner = Spinners.arc  # spinner type
                sp.start()
                sp.text = "Fetching related informations"    # text along with spinner
                sp.color = "green"         # spinner color
                sp.side = "right"          # put spinner to the right
                sp.reversal = True         # reverse spin direction
                completion = openai.Completion.create(
                    model = model_name,
                    prompt = order,
                    max_tokens = 1024,
                    n=1,
                    stop = None)
                response = completion.choices[0].text.split('.')
                sp.ok()
                for answer in response:
                    speak(answer)
            except Exception as e:
                sp.fail()
                print(e)
        else:
            sp.ok()
            speak('Okay sir, tell me your queries please.')
            from takecommand import take_command
            command = take_command()
            try:
                import openai
                sp.start()
                openai.api_key = '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'
                model_name = 'text-davinci-003'
                sp.ok()
                sp.spinner = Spinners.arc  # spinner type
                sp.start()
                sp.text = "Fetching related informations"    # text along with spinner
                sp.color = "green"         # spinner color
                sp.side = "right"          # put spinner to the right
                sp.reversal = True         # reverse spin direction
                completion = openai.Completion.create(
                    model = model_name,
                    prompt = command,
                    max_tokens = 1024,
                    n=1,
                    stop = None
                )
                response = completion.choices[0].text.split('.')
                sp.ok()
                for answer in response:
                    speak(answer)
            except:
                sp.fail()