import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 object

        # Set the voice property to german voice
        self.__voices = self.engine.getProperty('voices')  # Store all the available voices into a list

        # Set voice to desired language
        for voice in self.__voices:
            if voice.id == 'german':
                self.engine.setProperty('voice', voice.id)
                break

    # Function for returning certain text as speech
    def speak_text(self, text_data):
        if text_data != '':
            self.engine.say(text_data)
            self.engine.runAndWait()
