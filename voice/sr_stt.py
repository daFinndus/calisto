import speech_recognition as sr
import sounddevice  # This is hella important, keeps away a lot of error messages

sounddevice.sleep(0)  # Random line of code to keep sounddevice


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # Function to print all available microphones
    def use_microphone_list(self, method):  # Method to check what we want to do with the microphone_list
        mic_list = self.microphone.list_microphone_names()
        if method == "get":
            return mic_list
        elif method == "print":
            for mic in enumerate(mic_list):
                print(mic)

    # Function to set our microphone to the HyperX mic
    def set_to_microphone(self, mic_name, mic_list):
        for index, mic in enumerate(mic_list):
            if mic_name in mic:
                self.microphone = sr.Microphone(index)
                print(f"Set {mic} as the new source.")

    # Function to listen to sound and translate it into words
    def listen_to_source(self):
        print("Listening now...")
        with self.microphone as source:
            audio_data = self.recognizer.listen(source)
        return audio_data

    # Function to print audio_data
    def print_audio(self, audio_data):
        # Translate our audio_data into words with vosk
        translated_audio_data = self.recognizer.recognize_google(audio_data, "de-DE")

        print(f"I understood: {translated_audio_data}")
