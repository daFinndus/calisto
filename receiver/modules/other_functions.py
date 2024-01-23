import os

from datetime import datetime


# Class for other functions
class OtherFunctions:
    def __init__(self):
        pass

    def get_current_time(self):
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def get_temperature_of_pi(self):
        # Get the temperature of the raspberry pi
        temp = os.popen("vcgencmd measure_temp").readline()
        return temp.replace("temp=", "").replace("'C\n", "")
