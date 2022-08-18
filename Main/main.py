from csv import QUOTE_ALL
from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic



class UI(QWidget):
    def __init__(self):
        super().__init__()


        uic.loadUi('YTDWindowUI.ui',self)


# Our app
app = QApplication(sys.argv)
# Our app window and visibile
window = UI()
window.show





# app execution
app.exec()