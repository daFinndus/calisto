import random

from modules.other_functions import OtherFunctions
from modules.stepper_motor import StepperMotor
from modules.temp_sens import TempSensor


class Response:
    def __init__(self):
        self.stepper_motor = StepperMotor()
        self.temp_sensor = TempSensor(1, 64)
        self.other_functions = OtherFunctions()

        self.function_dict = {
            'motor': {
                'function': self.stepper_motor.do_clockwise_degrees,
                'return': [
                    f'Der Motor dreht sich nun.',
                    f'Ich habe den Motor gedreht.',
                    f'Ich habe den Motor bewegt.',
                ]
            },
            'temperature': {
                'function': self.temp_sensor.measure_temp,
                'return': [
                    f'Die Temperatur beträgt',
                    f'Aktuell sind es',
                    f'Wir haben gerade',
                ],
            },
            "time": {
                "function": self.other_functions.get_current_time,
                "return": [
                    f'Die aktuelle Uhrzeit ist',
                    f'Es ist momentan',
                    f'Jetzt ist es'
                    f'Wir haben gerade'
                ],
            },
            'pi-temp': {
                'function': self.other_functions.get_temperature_of_pi,
                'return': [
                    f'Die Temperatur des Raspberry Pi beträgt',
                    f'Der Raspberry Pi hat',
                    f'Mein Prozessor hat eine Temperatur von'
                ],
            }
        }

        self.responses_dict = {
            'greeting': ['Hallo!', 'Hi!', 'Guten Tag!', 'Moin moin!'],
            'feeling': [
                'Mir geht es gut!', 'Mir geht es schlecht.', 'Wundervoll!', 'Ich bin müde.', 'Ich bin gut drauf.',
                'Mir geht es spitze.', 'Ich bin gut gelaunt.', 'Ich bin schlecht gelaunt.', 'Ich bin traurig.',
            ],
        }

        self.error_list = [
            'Ich habe dich nicht verstanden.',
            'Bitte wiederhole deine Eingabe.',
            'Es ist ein Fehler aufgetreten.',
            'Tut mir leid, ich kann dir nicht folgen.',
            'Ich verstehe dich nicht.',
            'Bitte achte auf das Skript.',
            'Etwas deutlicher reden bitte.'
        ]

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
        print(f'Function: {function}')
        amount = json_object['amount'] if 'amount' in json_object else None
        print(f'Amount: {amount}')

        if function == 'temperature':
            return f'{random.choice(self.function_dict[function]["return"])} {self.temp_sensor.measure_temp()} Grad Celsius.'
        elif function == 'time':
            return f'{random.choice(self.function_dict[function]["return"])} {self.function_dict[function]["function"]()} Uhr.'
        elif function == 'pi-temp':
            return f'{random.choice(self.function_dict[function]["return"])} {self.function_dict[function]["function"]()} Grad Celsius.'
        # Execute the function with the given amount
        elif function == 'motor' and amount is not None:
            self.function_dict[function]['function'](amount)
            return random.choice(self.function_dict[function]['return'])
        # Choose a random value if no amount is given
        elif function == 'motor' and amount is None:
            self.function_dict[function]['function'](random.randint(45, 180))
            return random.choice(self.function_dict[function]['return'])

    # This should work as expected
    def execute_response(self, json_object):
        keyword = json_object['keyword']
        details = json_object['details']

        for response_entry in self.responses_dict:
            if keyword == response_entry:
                return random.choice(self.responses_dict[response_entry])
