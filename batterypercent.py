from speak import speak
from desktop_notify import desktop_notify
import psutil


def check_power():
    is_charging = psutil.sensors_battery().power_plugged
    battery_percentage = psutil.sensors_battery().percent 
    if is_charging:
        speak(f'Sir, our system have {battery_percentage} % power and the system is plugged in.')
    elif battery_percentage >= 80:
        speak(f'Sir, our system have {battery_percentage} % power and we have enough power to continue our work.')
    elif battery_percentage >= 50:
        speak(f'Sir, our system have {battery_percentage} % power and we should connect our system to charging point.')
    elif battery_percentage >= 25:
        speak(f'Sir, our system have {battery_percentage} % power and we have very lower power, maybe we should connect to charger as soon as possible.')
    else:
        speak(f'Sir, our system have {battery_percentage} % power and we have very lower power so system is  going to shutdown in few minutes. ')
    desktop_notify('Battery Status', f'Battery: {battery_percentage}%')