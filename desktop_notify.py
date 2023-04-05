from plyer import notification
def desktop_notify(title,message):
    '''this function uses plyer module to show notification on desktop screen. It taks title and message to display in desktop as argument'''
    notification.notify(title=title,message=message,timeout = 10, app_icon = 'bell.ico')