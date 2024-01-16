import json
import sys
import threading

from uart_receiver import MyUart
from tts.py_tts_x3 import TextToSpeech
from gui.gui_functions import Functions_PyGUI
from gui.gui import Ui_MainWindow
from PyQt5 import QtWidgets
from to_response import Response


# FIXME: Sometimes output is empty, that throws an error
# Listen for something via uart and text-to-speech it
def get_data_and_speak():
    while True:
        data = uart.read_data()
        # Show if we got data or not
        print(f'Got data: {data}') if data else print('No data received...')
        if data:
            print('If-Statement entered')
            try:
                # Format json string to json object
                json_object = json.loads(data)
                print(f'Parsed JSON: {json_object}')
                py_gui.change_input(json_object['input'])
                # Create a response
                response_data = response.to_response(json_object['output'])
                print(f'Response: {response_data}')
                py_gui.change_output(response_data)
                tts.speak_text(response_data)
            except Exception as e:
                print(f'Error processing JSON: {e}')


if __name__ == '__main__':
    tts = TextToSpeech()
    response = Response()
    uart = MyUart('/dev/ttyS0')

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    py_gui = Functions_PyGUI(Ui_MainWindow, Dialog, uart)

    threading.Thread(target=get_data_and_speak).start()

    Dialog.show()  # Show our window
    sys.exit(app.exec_())
