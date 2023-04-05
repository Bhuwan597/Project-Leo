import speedtest
import math
from yaspin.spinners import Spinners
from yaspin import yaspin
from speak import speak
import requests
def check_internet_speed():
    speak('Sir, give me few seconds to analyze your internet speed.')
    with yaspin(Spinners.noise, text=f'Checking your internet speed') as sp:
        try:
            ip = requests.get('https://api.ipify.org').text
            url='https://get.geojs.io/v1/ip/geo/'+ ip + '.json'
            info  = requests.get(url).json()
            connection = info['organization_name']
            sp.spinner = Spinners.arc  # spinner type
            sp.text = f"{connection}"    # text along with spinner
            sp.color = "green"         # spinner color
            sp.side = "right"          # put spinner to the right
            sp.reversal = True         # reverse spin direction
            st = speedtest.Speedtest()
            upload_speed = math.ceil(st.upload()/(1000000)) 
            download_speed =  math.ceil(st.download()/(1000000)) 
            ping = math.ceil(st.results.ping)
            sp.ok() 
            speak(f"Your internet have upload speed of {upload_speed} megabytes per second, download speed of {download_speed} megabytes per second and latency of {ping} from {connection}")
            from desktop_notify import desktop_notify
            desktop_notify(f'Internet Speed {connection}',f"Upload speed: {upload_speed} MB/s\nDownload speed: {download_speed} MB/s\nLatency: {ping}")
        except:
            speak('\nSorry sir, some error occured while analayzing internet speed.')