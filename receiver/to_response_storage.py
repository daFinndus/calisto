from modules.other_functions import OtherFunctions
from modules.stepper_motor import StepperMotor
from modules.temp_sens import TempSensor


# This class stores important data for the receiver side application
class ResponseStorage:
    def __init__(self):
        self.stepper_motor = StepperMotor()
        self.temp_sensor = TempSensor(1, 64)
        self.other_functions = OtherFunctions()

        self.function_dict = {
            'motor': {
                'function': (self.stepper_motor.do_clockwise_degrees, self.stepper_motor.do_counterclockwise_degrees),
                'direction': ['minus', 'zurück', 'gegen den uhrzeigersinn', 'gegen den uhrzeiger'],
                'return': [
                    f'Dem Schrittmotor ist nun schwindelig.',
                    f'Der Motor hat sich fertig bewegt.',
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
                    f'Jetzt ist es',
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

        # Intro, ready and abilities are not tested yet
        self.responses_dict = {
            'introduction': ['Hallo. Ich bin ein Sprachassistent von Finn, Darren und Jonas.'],
            'ready': ['Ich bin bereit.', 'Ich bin startklar.', 'Wir können loslegen.'],
            'abilities': [
                'Ich kann dir die Temperatur ausgeben, den Motor bewegen, mich mit dir unterhalten und und und.'],
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
