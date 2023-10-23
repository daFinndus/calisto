"""
Program that looks for voice input, works with it and answers with a voice output
"""

import os
import time
from time import sleep

from modules.led import LED
from modules.button import Button

from voice.py_tts_x3 import TextToSpeech as pyTTS
from voice.vosk_stt import SpeechToText as voskSTT

project_dir = os.path.dirname(os.path.abspath("main.py"))
voice_dir = os.path.join(project_dir, "voice")
model_dir = os.path.join(project_dir, "model")

vosk_stt = voskSTT(model_dir)
tts = pyTTS()

led = LED(11)
led.set_intensity(15)

button = Button()

print("Starting...\n")
sleep(0.5)


# Listens for audio and then speaks it out loud
def listen_and_speak():
    while True:
        audio_data = vosk_stt.get_audio_data()
        tts.speak_text(audio_data)


# Turns on light, then off, repeatedly
def light_on():
    while True:
        led.set_intensity(255)
        time.sleep(3)
        led.set_intensity(15)
        time.sleep(3)


if __name__ == "__main__":
    pass
