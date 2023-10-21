import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 object
        self.voices = self.engine.getProperty('voices')  # Store all the available voices into a list
        self.engine.setProperty('voice', self.voices[1].id)  # Set voice to german

    # Function to get the current speaking rate
    def get_speaking_rate(self, method):
        rate = self.engine.getProperty("rate")

        if method == "get":
            return rate
        elif method == "print":
            print(f"The current rate is: {rate}")

    # Function to do something with the volume
    def get_volume(self, method):
        volume = self.engine.getProperty("volume")

        if method == "get":
            return volume
        elif method == "print":
            print(f"The current volume is: {volume}")

    # Function to do something with the available voices
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

    # Save the spoken text to a file
    def save_to_file(self):
        self.engine.save_to_file("Sample", "voice.mp3")
