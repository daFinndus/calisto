import json
import pyaudio
from vosk import Model, KaldiRecognizer


# Our class for speech to text
class SpeechToText:
    def __init__(self, model_path):
        self._model = Model(model_path)  # Set the model for vosk with a certain path
        self._recognizer = KaldiRecognizer(self._model, 16000)  # Set up the recognizer

        self._pyaudio = pyaudio.PyAudio()  # Initialize the pyaudio object
        self._input_index = 1  # Set the input device

        self._format = pyaudio.paInt16  # Sampling size and format
        self._channels = 1  # Number of channels
        self._input = True  # Specifies whether this is an input stream

        # Rate in Hz is fixed to our chosen input device
        self._rate = 16000

    # Function to listen for audio data and returning it as a string
    def get_audio_data(self):
        # Open the microphone stream
        __stream = self._pyaudio.open(format=self._format, channels=self._channels, rate=self._rate, input=self._input)

        print("Listening...")

        try:
            while True:
                # Read data with certain chunk rate
                __data = __stream.read(4096)
                # Stop the while loop if no audio data is heard
                if len(__data) == 0:
                    print("Cannot hear any audio.")
                    break
                # If the vosk recognizer can do something with our audio
                if self._recognizer.AcceptWaveform(__data):
                    # Save our result in a variable
                    result = json.loads(self._recognizer.Result())
                    # Return our result
                    return result
        except KeyboardInterrupt:
            pass
        finally:
            __stream.stop_stream()
            __stream.close()
