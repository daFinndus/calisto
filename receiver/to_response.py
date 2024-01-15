import random

from modules.temp_sens import TempSensor


class Response:
    def __init__(self):
        self.temp_sensor = TempSensor(1, 64)

        # TODO: Also implement the motor
        self.function_dict = {
            ("temperatur",): {
                "function": self.temp_sensor.measure_temp,
                "return": [
                    f'Die Temperatur beträgt {self.temp_sensor.measure_temp()} Grad Celsius.',
                    f'Aktuell sind es {self.temp_sensor.measure_temp()} Grad Celsius.',
                    f'Wir haben gerade {self.temp_sensor.measure_temp()} Grad Celsius.'
                ],
            },
        }

        self.error_list = [
            'Ich habe dich nicht verstanden.',
            'Bitte wiederhole deine Eingabe.',
            'Es ist ein Fehler aufgetreten.',
            'Tut mir leid, ich kann dir nicht folgen.'
        ]

        # TODO: Create more responses
        self.responses_dict = {
            'greeting': ["Hallo!", "Hi!", "Guten Tag!", "Moin moin!"],
            'feeling': ["Mir geht es gut!", "Mir geht es schlecht.", "Wundervoll!"],
        }

    # This function chooses a response based on the input string
    def to_response(self, json_object):
        if json_object['type'] == 'response':
            self.execute_response(json_object)
        elif json_object['type'] == 'function':
            return self.execute_function(json_object)
        else:
            return random.choice(self.error_list)

            # This function is for executing functions

    def execute_function(self, json_object):
        function = json_object['keyword']
        amount = json_object['amount'] if 'amount' in json_object else None

        for function_entry in self.function_dict:
            if function == function_entry and amount is None:
                function_entry['function']()
            else:
                function_entry['function'](amount)
            return random.choice(function_entry['return'])

    def execute_response(self, json_object):
        keyword = json_object['keyword']
        details = json_object['details']

        for response_entry in self.responses_dict:
            if keyword == response_entry:
                return random.choice(self.responses_dict[response_entry])
