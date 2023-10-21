import json
import pyaudio
from vosk import Model, KaldiRecognizer


class SpeechToText:
    def __init__(self, model_path):
        self.model = Model(model_path)  # Set the model for vosk with a certain path
        self.recognizer = KaldiRecognizer(self.model, 16000)  # Set up the recognizer

        self.pyaudio = pyaudio.PyAudio()  # Initialize the pyaudio object
        self.input_index = 1  # Set the input device

        self.format = pyaudio.paInt16  # Sampling size and format
        self.channels = 1  # Number of channels
        self.input = True  # Specifies whether this is an input stream

        # Sampling rate in Hz is fixed to our chosen input device
        self.rate = 16000

        self.keyword = "Calisto"  # Custom keyword as wake word
        self.keyword_detected = False  # Boolean to detect if the keyword is detected

    # Function to get all available microphones
    def get_microphone_list(self, method):  # Method to check what we want to do with the microphone_list
        mic_list = []  # Store all available mics in a list
        mic_amount = self.pyaudio.get_device_count()  # Outputs how many mics are available as an integer
        for mic in range(mic_amount):
            mic_name = self.pyaudio.get_device_info_by_index(mic)  # Display information about the mic
            mic_list.append(mic_name.get("name"))  # Add the mic name to our list

        if method == "get":
            return mic_list
        elif method == "print":
            print(mic_list)

    # Function to give information about the current microphone used
    def get_microphone_info(self):
        print(self.pyaudio.get_device_info_by_index(self.input_index))

    # Function to set our microphone to a specified microphone
    def set_microphone_device(self, mic_name, mic_list):
        # Numerate all our entries in mic_list
        for index, mic in enumerate(mic_list):
            # Go through every mic entry until mic_name is detected
            if mic_name in mic:
                # Update our device to certain index
                self.input_index = index
                print(f"Updated device input to: {mic_list[index]}")

    # Function to listen for audio data
    def listen_for_prompt(self):
        # Open the microphone stream
        stream = self.pyaudio.open(format=self.format, channels=self.channels, rate=self.rate, input=self.input)

        print("Listening...")

        try:
            while True:
                # Read data with certain chunk rate
                data = stream.read(4096)
                # Stop the while loop if no audio data is heard
                if len(data) == 0:
                    print("Cannot hear any audio.")
                    break
                # If the vosk recognizer can do something with our audio
                if self.recognizer.AcceptWaveform(data):
                    # Save our result in a variable
                    result = json.loads(self.recognizer.Result())
                    # Extract the text
                    text = result["text"]
                    print(text)
                    return text
        except KeyboardInterrupt:
            pass
        finally:
            stream.stop_stream()
            stream.close()

    # Function to print audio_data
    @staticmethod
    def print_audio(audio_data):
        print(audio_data)
