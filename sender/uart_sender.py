import threading
import serial


# Class for sending data via uart
class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port
        self.thread_send = threading.Thread(target=self.send_data)

    # Function to sending strings as bytes
    def send_data(self, data):
        try:
            self.ser.write(data.encode())
        except Exception as e:
            print(e)
            return 'Error while sending data via uart'
