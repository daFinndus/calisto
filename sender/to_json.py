import json


class JSON:
    def __init__(self):
        self.data_edited = False

        self.function_list = {('motor', 'schrittmotor'), 'temperatur'}

        self.response_dict = {
            ('hallo', 'moin', 'hi', 'hey', 'guten tag'): 'greeting',
            ('wie geht es dir', 'wie gehts dir', 'wie geht es', "wie geht's"): 'feeling',
        }

    def to_json(self, data):
        self.data_edited = False

        json_object = {'input': data,
                       'output': ()}

        response_info = self.detect_response(data)
        if response_info is not None:
            json_object.update(response_info)

        function_info = self.detect_function(data)
        if function_info is not None:
            json_object.update(function_info)

        json_string = json.dumps(json_object)
        return json_string

    # TODO: It always detects temperatur, if nothing else gets detected, why?
    # Detect function keywords, if found, return a json object
    def detect_function(self, data):
        data = data.lower()
        data_single = data.split(' ')

        json_object = {}

        if not self.data_edited:
            for function_entries in self.function_list:
                # Format tuples into strings if they are tuples
                function = ' '.join(function_entries) if isinstance(function_entries, tuple) else function_entries
                if function in data:
                    print(f"Found function: {function}")
                    json_object['type'] = 'function'
                    json_object['keyword'] = function
                    # Check if data contains a number
                    if 'motor' in function:
                        for strings in data_single:
                            try:
                                int(strings)
                                if strings.isdigit():
                                    json_object['amount'] = strings
                            except ValueError:
                                pass
                    self.data_edited = True
                    return {'output': json_object}
                else:
                    print(f"Didn't find function: {function}")

    # Detect response keywords, if found, return a json object
    # FIXME: They also detect something like 'ich' in 'mich', fix that
    def detect_response(self, data):
        data = data.lower()
        data_single = data.split(' ')

        json_object = {}

        if not self.data_edited:
            for response_entries in self.response_dict:
                for response in response_entries:
                    if response in data:
                        print(f"Found response: {response}")
                        json_object['type'] = 'response'
                        json_object['details'] = self.response_dict[response_entries]
                        json_object['keyword'] = response
                        self.data_edited = True
                        return {'output': json_object}
                    else:
                        print(f"Didn't find response: {response}")
