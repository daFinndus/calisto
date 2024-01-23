import pyttsx3


# Class for playing a certain string via the speaker
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 object

        # Set the voice property to german voice
        self.__voices = self.engine.getProperty('voices')  # Store all the available voices into a list
        self.__language = 'german'  # This is the language we want to use

        # Set voice to desired language
        for voice in self.__voices:
            if voice.id == self.__language:
                self.engine.setProperty('voice', voice.id)
                break

    # Function for returning certain text as audio
    def speak_text(self, text_data):
        if text_data != '':
            self.engine.say(text_data)
            self.engine.runAndWait()
