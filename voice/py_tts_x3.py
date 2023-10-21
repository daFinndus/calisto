import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 object

    # Function to get the current speaking rate
    def get_speaking_rate(self, method):
        rate = self.engine.getProperty("rate")

        if method == "get":
            return rate
        elif method == "print":
            print(f"The current rate is: {rate}")

    def get_volume(self, method):
        volume = self.engine.getProperty("volume")

        if method == "get":
            return volume
        elif method == "print":
            print(f"The current volume is: {volume}")

    def get_voices(self, method):
        voices = self.engine.getProperty("voices")

        if method == "get":
            return voices
        if method == "print":
            for voice in voices:
                print(voice)

    # Function for returning certain text as speech
    def speak_text(self, text_data):
        self.engine.say(text_data)
        self.engine.runAndWait()

    def save_to_file(self):
        self.engine.save_to_file("Sample", "voice.mp3")
