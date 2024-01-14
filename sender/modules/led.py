from RPi import GPIO


class LED:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)  # Address pins with their numbers
        GPIO.setwarnings(False)  # Mute all these irrelevant warnings, don't need them anyway
        GPIO.setup(pin, GPIO.OUT)  # Set pins as output

        self._pwm_object = GPIO.PWM(pin, 100)  # Initialize object with 100hz
        self._pwm_object.start(0)  # Start the pwm_object

        self.__intensity = 0  # Private object to calibrate LEDs
        self.__pin = pin  # Private object for setting the pin

        print(f"LED-Device setup for pin {pin} is complete.")
        print(f"The LED is starting with an intensity of {self.__intensity}.\n")

    # Set the intensity to a certain value and translate it into percent
    def set_intensity(self, value):
        if value in range(0, 256):
            self.__intensity = value
            self._pwm_object.ChangeDutyCycle(
                100 - (self.__intensity / 255 * 100))  # Set duty cycle as difference to a hundred percent
        else:
            self.__intensity = 0
            print("\nWarning: The intensity value is not between 0 and 255.")
            print("Please enter a number between 0 and 255.\n")

    # Function to turn off the pwm_object
    def switch_off(self):
        self._pwm_object.stop()
        GPIO.output(self.__pin, False)
        print("Turned off pwm_object.")

    # Change certain pin to input
    @staticmethod
    def clean_up_pin(pin):
        GPIO.cleanup(pin)
        print(f"\nCleaned pin {pin}.")

    # Change all outputs to inputs
    @staticmethod
    def clean_up_gpio():
        GPIO.cleanup()
        print(f"Changed all pins to IN.")
