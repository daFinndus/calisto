import json
import threading

import numpy as np
import pyaudio
from vosk import Model, KaldiRecognizer


class SpeechToText:
    def __init__(self, model_path):
        self.model = Model(model_path)  # Set the model for vosk with a certain path
        self.recognizer = KaldiRecognizer(self.model, 16000)  # Set up the recognizer

        self.pyaudio = pyaudio.PyAudio()  # Initialize the pyaudio object
        self.input_device_index = 1  # Set the input device

        self.format = pyaudio.paInt16  # Sampling size and format
        self.channels = 1  # Number of channels
        self.chunk = 4096  # Number of frames per buffer
        self.rate = 44100  # Sampling rate
        self.input = True  # Specifies whether this is an input stream

        self.keyword = "Calisto"

        self.keyword_detected = False

    # Function to print all available microphones
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

    # Function to set our microphone to a specified microphone
    def set_microphone_device(self, mic_name, mic_list):
        # Numerate all our entries in mic_list
        for index, mic in enumerate(mic_list):
            # Go through every mic entry until mic_name is detected
            if mic_name in mic:
                # Update our device to certain index
                self.input_device_index = index
                print(f"Updated device input to: {mic_list[index]}")

    # Function to give information about the current microphone used
    def get_microphone_info(self):
        print(self.pyaudio.get_device_info_by_index(self.input_device_index))

    def recognize(self, data):
        if self.recognizer.AcceptWaveform(data):
            result = json.loads(self.recognizer.Result())
            print(f"Heard something... {result}")

            if self.keyword in result["text"].lower():
                self.keyword_detected = True
                print("Keyword detected! Starting application...")

    def listen_for_keyword(self):

        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=self.input,
            input_device_index=self.input_device_index,
        )

        while not self.keyword_detected:
            data = stream.read(self.chunk, exception_on_overflow=False)

            rms = np.sqrt(np.mean(np.frombuffer(data, dtype=np.int16) ** 2))
            print(f"Threshold right now: {rms}")

            if rms > 30.0:
                print("Reached threshold...")

                # Initialize recognition thread
                recognition_thread = threading.Thread(target=self.recognize, args=(data,))

                # Start a new thread for recognition process if not already running
                if not recognition_thread.is_alive():
                    recognition_thread.start()

            if len(data) == 0:
                print("No data received.")

    # Function to listen for tasks
    def listen_for_tasks(self):
        # Open the microphone stream
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=self.input,
            frames_per_buffer=self.chunk,
            input_device_index=self.input_device_index
        )

        print("Listening...")

        while True:
            # Store chunks of our audio queue into a variable -> The higher the parameter the longer the chunks
            data = stream.read(4096)
            # Check if data is empty -> No one is saying something
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                # Translate json string into python dictionary
                result = json.loads(self.recognizer.Result())
                # Set the keyword detection to False again
                self.keyword_detected = False
                # If the waveform is alright, return our result
                return result

    # Function to print audio_data
    @staticmethod
    def print_audio(audio_data):
        print(audio_data)
