# This class is for editing the GUI of the receiver
class Functions_PyGUI:
    def __init__(self, PyGUI, Dialog):
        self.ui = PyGUI()
        self.ui.setupUi(Dialog)

    # This function is for changing the text of the input line edit
    def change_input(self, text):
        self.ui.input_lineEdit.setText('')
        self.ui.input_lineEdit.setText(text)

    # This function is for changing the text of the output line edit
    def change_output(self, text):
        self.ui.output_lineEdit.setText('')
        self.ui.output_lineEdit.setText(text)
