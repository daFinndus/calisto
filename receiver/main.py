import sys
import threading

from uart_receiver import MyUart
from tts.py_tts_x3 import TextToSpeech
from gui.gui_functions import Functions_PyGUI
from gui.gui import Ui_MainWindow
from PyQt5 import QtWidgets


# Listen for something via uart and tts it
def get_data_and_speak():
    while True:
        data = uart.read_data()
        print("Received data:", data)
        if data:
            print("Processing data:", data)
            py_gui.change_input(data)
            py_gui.change_output(data)
            tts.speak_text(data)
        data = ''  # Clear data


if __name__ == '__main__':
    tts = TextToSpeech()
    uart = MyUart('/dev/ttyAMA0')

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    py_gui = Functions_PyGUI(Ui_MainWindow, Dialog, uart)

    threading.Thread(target=get_data_and_speak).start()

    Dialog.show()  # Show our window
    sys.exit(app.exec_())
