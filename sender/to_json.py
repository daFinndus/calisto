import json
import text2numde

from to_json_storage import JsonStorage


# This class is used for converting the data from the speech to text module into a json string
class JSON:
    def __init__(self):
        self.data_edited = False
        self.storage = JsonStorage()

        self.function_dict = self.storage.function_dict
        self.response_dict = self.storage.response_dict

    def to_json(self, data):
        self.data_edited = False

        json_object = {'input': data,
                       'output': ()}

        # Check if data contains a response
        response_info = self.detect_response(data)
        if response_info is not None:
            json_object.update(response_info)

        # If data wasn't a response, check for function
        function_info = self.detect_function(data)
        if function_info is not None:
            json_object.update(function_info)

        # If data wasn't a response or a function, return an error
        if not response_info and not function_info:
            print('No response or function found, going to implement an error.')
            error_info = {'output': {'type': 'error'}}
            json_object.update(error_info)

        json_string = json.dumps(json_object)
        return json_string

    # Detect function keywords, if found, return a json object
    def detect_function(self, data):
        data = data.lower()
        data_split_list = data.split(' ')

        json_object = {}

        if not self.data_edited:
            for function_entry in self.function_dict:
                for function in function_entry:
                    if function in data:
                        try:
                            json_object['type'] = 'function'
                            json_object['keyword'] = self.function_dict[function_entry]
                            json_object['details'] = data
                            # Check if data contains a number
                            if self.function_dict[function_entry] == 'motor':
                                # Go through every word and try to find numbers
                                for data_split in data_split_list:
                                    try:
                                        # Convert words into real numbers
                                        data_split = text2numde.text2num(data_split)
                                        print(type(data_split))
                                        if isinstance(data_split, int):
                                            print(f'Found amount: {data_split}')
                                            json_object['amount'] = data_split
                                    except Exception as e:
                                        print(f'Error while text2numde: {e}')
                            self.data_edited = True
                            return {'output': json_object}
                        except Exception as e:
                            print(f'Error while generating function object: {e}')

    # Detect response keywords, if found, return a json object
    def detect_response(self, data):
        data = data.lower()

        json_object = {}

        if not self.data_edited:
            for response_entry in self.response_dict:
                for response in response_entry:
                    if response in data:
                        try:
                            json_object['type'] = 'response'
                            json_object['keyword'] = self.response_dict[response_entry]
                            json_object['details'] = response
                            self.data_edited = True
                            return {'output': json_object}
                        except Exception as e:
                            print(f'Error while generating response object: {e}')
