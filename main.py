"""
Program that looks for voice input, works with it and answers with a voice output
"""

import os
from time import sleep

from voice.py_tts_x3 import TextToSpeech as pyTTS
from voice.vosk_stt import SpeechToText as voskSTT

"""from voice.sr_stt import SpeechToText as srSTT"""

project_dir = os.path.dirname(os.path.abspath("main.py"))
voice_dir = os.path.join(project_dir, "voice")
model_dir = os.path.join(project_dir, "model")

vosk_stt = voskSTT(model_dir)
tts = pyTTS()

print("Starting...\n")
sleep(0.5)

vosk_stt.listen_and_print()
