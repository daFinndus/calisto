class Functions_PyGUI:
    def __init__(self, PyGUI, Dialog, uart):
        self.ui = PyGUI()
        self.ui.setupUi(Dialog)

        self.uart = uart

    def change_input(self, text):
        self.ui.input_lineEdit.setText('')
        self.ui.input_lineEdit.setText(text)

    def change_output(self, text):
        self.ui.output_lineEdit.setText('')
        self.ui.output_lineEdit.setText(text)


