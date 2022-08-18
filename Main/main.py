from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys
from PyQt6 import uic
import pathlib


path = pathlib.Path(__file__).parent.resolve()


#* create main class for the app UI
class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{path}/YTDWindowUI.ui',self)





#* Our app
app = QApplication(sys.argv)
#* Our app window and visibile
window = UI()
window.show()





#* app execution
sys.exit(app.exec())