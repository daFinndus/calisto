# This class stores important data for the sender side application
class JsonStorage:
    def __init__(self):
        self.function_dict = {
            ('bewege den motor', 'dreh den motor'): 'motor',
            ('zeig mir die temperatur', 'wie warm ist es'): 'temperature',
            ('wie spät ist es', 'welche uhrzeit haben wir'): 'time',
            ('wie warm bist du', 'wie heiß ist dein prozessor'): 'pi-temp',
        }

        self.response_dict = {
            ('wer bist du', 'stell dich vor', 'was bist du'): 'introduction',
            ('bist du bereit', 'kann es losgehen', 'können wir starten'): 'ready',
            ('was kannst du', 'was für funktionen hast du'): 'abilities',
            ('hallo', 'moin', 'hi', 'hey', 'guten tag'): 'greeting',
            ('wie geht es dir', 'wie gehts dir', 'wie gehts'): 'feeling',
        }
