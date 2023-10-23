import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 object

        # Set the voice property to german voice
        self.__voices = self.engine.getProperty('voices')  # Store all the available voices into a list
        self.engine.setProperty('voice', self.__voices[1].id)  # Set voice to german

    # Function to get the current speaking rate
    def get_rate(self):
        rate = self.engine.getProperty("rate")
        return rate

    # Function to return the current volume
    def get_volume(self):
        volume = self.engine.getProperty("volume")
        return volume

    # Function to get the voices
    def get_voices(self):
        voices = self.engine.getProperty("voices")
        return voices

    # Function for returning certain text as speech
    def speak_text(self, text_data):
        self.engine.say(text_data)
        self.engine.runAndWait()

    # Save the spoken text to a file
    def save_to_file(self):
        self.engine.save_to_file("Sample", "voice.mp3")
