# User interface of interactions

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor
import sys
from numpy import rec

from pyparsing import col


class Window(QWidget):

	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Guessing Word Game :)")
		self.setFixedSize(410, 610)
		self.setStyleSheet("background:#809292")

		layout = QVBoxLayout()
		self.setLayout(layout)

		#create label
		timeLabel = QLabel("Time")
		timeLabel.setFixedSize(100, 43)
		timeLabel.setStyleSheet("Background:#A3A798; padding-left:20px; padding-right:20px")

		gameTitleLabel = QLabel("Guessing Game :)")
		gameTitleLabel.setFixedSize(253, 62)
		gameTitleLabel.setStyleSheet("background:#ABCCD8; border-radius:20px; padding-left:15px")

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
		
		



		
