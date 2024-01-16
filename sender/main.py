import os
import time

from to_json import JSON
from modules.led import LED
from modules.button import Button
from uart_sender import MyUart
from stt.vosk_stt import SpeechToText as voskSTT

project_dir = os.path.dirname(os.path.abspath("main.py"))
model_dir = os.path.join(project_dir, "model")

json = JSON()

stt = voskSTT(model_dir)
uart = MyUart('/dev/ttyS0')

button = Button(16)
led = LED(11)


# This function should be executed by pressing a button
def speak_and_send_data():
    led.set_intensity(255)
    data = stt.get_audio_data()['text']
    print(f'Raw data: {data}') if data else print('Sending no data.')
    data = json.to_json(data)
    print(f'Sending data: {data}') if data else None
    uart.send_data(data)
    led.set_intensity(0)


if __name__ == '__main__':
    # Make sure to turn 'off' the LED
    led.set_intensity(0)

    while True:
        if button.tap_button():
            speak_and_send_data()
            time.sleep(1)
