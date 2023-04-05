from speak import speak
from yaspin import yaspin
from yaspin.spinners import Spinners
import time
from requests import get
def find_location():
    speak('Wait sir, Let me find your location')
    with yaspin(Spinners.noise, text='Accessing location') as sp:
        try:
            ip_address = get('https://api.ipify.org').text
            url='https://get.geojs.io/v1/ip/geo/'+ ip_address + '.json'
            sp.spinner = Spinners.arc  # spinner type
            sp.text = "Finding your location"    # text along with spinner
            sp.color = "green"         # spinner color
            sp.side = "right"          # put spinner to the right
            sp.reversal = True         # reverse spin direction
            time.sleep(1)
            geo_array = get(url).json()
            city = geo_array['city']
            country = geo_array['country']
            sp.ok()
            speak(f'Your current location is in country {country} and {city} city.')
            from desktop_notify import desktop_notify
            desktop_notify('Current Location',f'Your current location is in country {country} and {city} city.')
        except:
            speak('Sorry sir, there was a problem on finding your location.')
            sp.fail()