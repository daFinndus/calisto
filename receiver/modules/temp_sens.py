import Adafruit_ADS1x15
import numpy as np


# Our class for the temperature sensor of our receiver pi
class TempSensor:
    def __init__(self, gain, samples_per_second):
        self.adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
        self.adc_channel = 0
        self.raw_data = None
        self.voltage_measurements = None
        self.gain = gain  # Set the gain to 1
        self.samples_per_second = samples_per_second  # Set the samples per second to 64

    # Function to measure the temperature
    def measure_temp(self):
        # Read the ADC
        self.raw_data = self.adc.read_adc(self.adc_channel, self.gain, self.samples_per_second)

        # Convert the ADC value to a voltage
        self.voltage_measurements = float(self.raw_data) / 32767.0 * 4.095

        # This is the Steinhart-Hart equation for converting the voltage to a temperature
        temp = 10000 / (3.3 / self.voltage_measurements - 1)
        temp = 1 / (0.001129148 + 0.000234125 * np.log(temp) + 0.0000000876741 * np.power(np.log(temp), 3))
        temp -= 273.15

        # Round the temperature to 2 decimal places for readability
        temp = round(temp, 2)

        return temp
