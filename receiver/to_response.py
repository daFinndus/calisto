import random

from to_response_storage import ResponseStorage
from modules.other_functions import OtherFunctions
from modules.stepper_motor import StepperMotor
from modules.temp_sens import TempSensor


# This class is used for converting the data from the json object to a response or a function, based on its content
class Response:
    def __init__(self):
        self.stepper_motor = StepperMotor()
        self.temp_sensor = TempSensor(1, 64)
        self.other_functions = OtherFunctions()
        self.storage = ResponseStorage()

        self.function_dict = self.storage.function_dict
        self.responses_dict = self.storage.responses_dict
        self.error_list = self.storage.error_list

    # This function chooses a response based on the input string
    def to_response(self, json_object):
        if json_object['type'] == 'response':
            return self.execute_response(json_object)
        elif json_object['type'] == 'function':
            return self.execute_function(json_object)
        elif json_object['type'] == 'error':
            return random.choice(self.error_list)
        else:
            return 'Es ist ein Fehler aufgetreten.'

    # This function is for executing functions
    def execute_function(self, json_object):
        function = json_object['keyword']
        amount = json_object['amount'] if 'amount' in json_object else random.randint(45, 180)

        if function == 'temperature':
            return f'{random.choice(self.function_dict[function]["return"])} {self.temp_sensor.measure_temp()} Grad Celsius.'
        elif function == 'time':
            return f'{random.choice(self.function_dict[function]["return"])} {self.function_dict[function]["function"]()} Uhr.'
        elif function == 'pi-temp':
            return f'{random.choice(self.function_dict[function]["return"])} {self.function_dict[function]["function"]()} Grad Celsius.'
        elif function == 'motor':
            # Create a new stepper motor object, because the old one is already cleaned up
            self.stepper_motor = StepperMotor()
            # Check if the motor should move clockwise or counterclockwise
            for direction in self.function_dict[function]['direction']:
                if direction in json_object['details']:
                    self.function_dict[function]['function'][1](amount)
                    self.stepper_motor.clean_up_gpio()
                    return random.choice(self.function_dict[function]["return"])

            # If none of the directions in our dict is in our details, we move clockwise
            self.function_dict[function]['function'][0](amount)
            self.stepper_motor.clean_up_gpio()
            return random.choice(self.function_dict[function]["return"])

    # This function is for getting a response
    def execute_response(self, json_object):
        keyword = json_object['keyword']
        details = json_object['details']

        for response_entry in self.responses_dict:
            if keyword == response_entry:
                return random.choice(self.responses_dict[response_entry])
