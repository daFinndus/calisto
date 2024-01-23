import serial


# Class for receiving data via uart
class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port

    # Function to read data from uart
    def read_data(self):
        try:
            data = self.ser.readline().decode('utf-8').strip()
            return data
        except Exception as e:
            print(e)
            return 'Error while reading data from uart'

    # Function to send data via uart
    def send_data(self, data):
        try:
            self.ser.write(data.encode())
        except Exception as e:
            print(e)
            return 'Error while sending data via uart'
