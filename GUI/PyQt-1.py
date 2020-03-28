import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Connecting to server')
label1 = QLabel('Please wait while connecting to server ...', parent = window)

window.show()

sys.exit(app.exec_())
