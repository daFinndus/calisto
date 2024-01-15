import Adafruit_ADS1x15
import numpy as np


class TempSensor:
    def __init__(self, gain, samples_per_second):
        self.adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
        self.adc_channel = 0
        self.raw_data = None
        self.voltage_measurements = None
        self.gain = gain  # Set the gain to 1
        self.samples_per_second = samples_per_second  # Set the samples per second to 64
        self.xs = []  # Create empty lists for our x values
        self.ys = []  # Create empty lists for our y values

    # Function to measure the temperature
    def measure_temp(self):
        # Read the ADC
        self.raw_data = self.adc.read_adc(self.adc_channel, self.gain, self.samples_per_second)

        # Convert the ADC value to a voltage
        self.voltage_measurements = float(self.raw_data) / 32767.0 * 4.095

        temp = np.log((10000 / self.voltage_measurements) * (3.3 - self.voltage_measurements))
        temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * np.power(temp, 2))) * temp)
        temp -= 273.15

        # Round the temperature to 2 decimal places for readability
        temp = round(temp, 2)

        return temp

    # Update data to our lists
    def update_data(self, temp):
        # Add '1' if nothing is in our list
        if not self.xs:
            self.xs.append(1)
        # Add '1' to our last entry in our list
        else:
            self.xs.append(self.xs[-1] + 1)
        # Add our temperature value to our list
        self.ys.append(temp)

    # Measure the temperature and update our lists
    def measure_and_update(self):
        temp = self.measure_temp()
        self.update_data(temp)
