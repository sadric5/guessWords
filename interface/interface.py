# User interface of interactions

from ctypes import alignment
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor
import sys


def clicked():
		print("Hello")

class Window(QWidget):



	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Guessing Word Game :)" )
		
		self.setFixedSize(410, 610)
		self.setStyleSheet("background:#225560")

		layout = QVBoxLayout()
		self.setLayout(layout)

		#create label
		timeLabel = QLabel("Time", alignment=Qt.AlignCenter)
		timeLabel.setFixedSize(100, 43)
		timeLabel.setStyleSheet("Background:#225560; padding-left:20px; padding-right:20px;")

		# print(timeLabel.getContentsMargins())

		gameTitleLabel = QLabel("Guessing Game :)", alignment=Qt.AlignCenter)
		gameTitleLabel.setFixedSize(253, 62)
		gameTitleLabel.setStyleSheet("background:#171219; border-radius:20px; padding-left:15px; color: white")

		username = QLineEdit()
		username.setPlaceholderText("Username")
		username.setMaxLength(25)
		username.setTextMargins(10, 10, 10, 10)
		username.setStyleSheet("background:#D3D3D3")

		passwordL = QLineEdit()
		passwordL.setPlaceholderText("Password")
		passwordL.setTextMargins(10, 10, 10, 10)
		passwordL.setStyleSheet("background:#D3D3D3")
		passwordL.setEchoMode(QLineEdit.EchoMode.Password)

		loginLabel = QPushButton("LOGIN")
		loginLabel.setFixedSize(152, 46)
		loginLabel.setStyleSheet("background:#8A997A; color:red")
		loginLabel.clicked.connect(clicked)
		loginLabel.move(10, 10)



		# add label to the window
		layout.addWidget(timeLabel, alignment= Qt.AlignRight)
		layout.addWidget(gameTitleLabel, alignment=Qt.AlignJustify)
		layout.addWidget(username, alignment=Qt.AlignJustify)
		layout.addWidget(passwordL, alignment=Qt.AlignJustify)
		layout.addWidget(loginLabel, alignment=Qt.AlignJustify)

	









if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screen = Window()
    screen.show()

    sys.exit(app.exec_())
		
		



		
