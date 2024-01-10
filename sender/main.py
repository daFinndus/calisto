import os
from stt.vosk_stt import SpeechToText as voskSTT

project_dir = os.path.dirname(os.path.abspath("main.py"))
model_dir = os.path.join(project_dir, "model")

if __name__ == "__main__":
    stt = voskSTT(model_dir)

    stt.print_audio(stt.get_audio_data()['text'])

