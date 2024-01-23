from RPi import GPIO
from time import sleep


# Our class for the button module of the sender pi
class Button:
    def __init__(self, pin):
        GPIO.setwarnings(False)  # Mute all these irrelevant warnings, don't need them anyway
        GPIO.setmode(GPIO.BOARD)  # Address pins with their numbers

        self.pin = pin

        # Change all button pins to inputs
        GPIO.setup(self.pin, GPIO.IN)
        print(f"Setup for pin {self.pin} is complete.")

        print(f"Setup for the buttons are completed.\n")

    # Function to check if a button is being pressed
    def tap_button(self):
        if GPIO.input(self.pin) == GPIO.LOW:
            sleep(0.5)
            return True
