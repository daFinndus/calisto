from RPi import GPIO
from time import sleep


class Button:
    def __init__(self):
        GPIO.setwarnings(False)  # Mute all these stupid warnings, don't need them anyway
        GPIO.setmode(GPIO.BOARD)

        # Create dictionary storaging button pins
        self.buttons = {
            "Button 1": 13,
            "Button 2": 15
        }

        # Change all button pins to inputs
        for pin in self.buttons.values():
            GPIO.setup(pin, GPIO.IN)
            print(f"Setup for pin {pin} is complete.")

        print(f"Setup for the buttons are completed.\n")

    # Function to check if a button is being pressed
    def tap_button(self):
        for pin in self.buttons.values():
            if GPIO.input(pin) == GPIO.HIGH:
                # print(f"Pin {pin} is being pressed.") # Debugging
                sleep(0.5)
                return True
