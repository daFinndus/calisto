import os
import time

from to_json import JSON
from modules.led import LED
from modules.button import Button
from uart_sender import MyUart
from stt.vosk_stt import SpeechToText as voskSTT

# Get the path of the module folder, the folder is necessary for the vosk library and contains a german model
project_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(project_dir, "model")

json = JSON()

stt = voskSTT(model_dir)
uart = MyUart('/dev/ttyS0')

button = Button(16)
button_bool = True  # A bool to en- and disable the button

led = LED(11)


# This function should be executed by pressing a button
# It is for listening to the user and sending the data to the receiver pi via uart
def speak_and_send_data():
    button_bool = False  # Disable the button for the following process
    led.set_intensity(255)
    data = stt.get_audio_data()['text']
    print(f'Raw data: {data}') if data else print('Sending no data.')
    data = json.to_json(data)
    print(f'Sending data: {data}') if data else None
    uart.send_data(data)
    wait_for_answer()
    button_bool = True  # Enable the button again
    led.set_intensity(0)


# Wait for the answer of the receiver side application
def wait_for_answer():
    while True:
        if uart.read_data() == 'finished':
            break


if __name__ == '__main__':
    # Make sure to turn 'off' the LED
    led.set_intensity(0)

    while True:
        # Activate the sender side application by pressing the button
        if button.tap_button() and button_bool:
            speak_and_send_data()
            time.sleep(1)
