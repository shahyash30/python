import time 
from plyer import notification

times = input("Schedule time for notification : ")

while(True):
    time.sleep(3600 * times)
    notification.notify(title = "water",message = "Drink water",timeout= 2 )
