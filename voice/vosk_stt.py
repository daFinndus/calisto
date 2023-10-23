import json
import pyaudio
from vosk import Model, KaldiRecognizer


class SpeechToText:
    def __init__(self, model_path):
        self._model = Model(model_path)  # Set the model for vosk with a certain path
        self._recognizer = KaldiRecognizer(self._model, 16000)  # Set up the recognizer

        self._pyaudio = pyaudio.PyAudio()  # Initialize the pyaudio object
        self._input_index = 1  # Set the input device

        self._format = pyaudio.paInt16  # Sampling size and format
        self._channels = 1  # Number of channels
        self._input = True  # Specifies whether this is an input stream

        # Sampling rate in Hz is fixed to our chosen input device
        self._rate = 16000

        self._keyword = "Calisto"  # Custom keyword as wake word
        self.keyword_detected = False  # Boolean to detect if the keyword is detected

    # Function to get all available microphones as a list
    def get_microphone_list(self):  # Method to check what we want to do with the microphone_list
        return [
            self._pyaudio.get_device_info_by_index(i).get("name")  # Get the name out of all available microphones
            for i in range(self._pyaudio.get_device_count())  # Go through every directory entry
        ]

    # Function to give information about the current microphone used
    def print_microphone_info(self):
        print(self._pyaudio.get_device_info_by_index(self._input_index))

    # Function to set our microphone
    def set_microphone_device(self, mic_name, mic_list):
        __matching_indices = [i for i, mic in enumerate(mic_list) if mic_name in mic]

        if __matching_indices:
            self._input_index = __matching_indices[0]
            print(f"Microphone device set to: {mic_list[self._input_index]}")
        else:
            print("Device not found.")

    # Function to listen for audio data
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

    # Function to print audio_data
    @staticmethod
    def print_audio(audio_data):
        print(audio_data)
