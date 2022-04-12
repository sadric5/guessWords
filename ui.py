# User interface of interactions

from ctypes import alignment
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor

import sys, os, random

# my module
from authentication import *


game =["Let's have fun !!!", "Let's relax :)", "Let's play"]

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.signIn = False

		self.setWindowTitle("Guessing Word Game :)" )
		self.setFixedSize(410, 610)
		self.setStyleSheet("background:#225560")
		self.login_ui()

	def basic_ui(self):
		self.mainC = QWidget()
		self.setCentralWidget(self.mainC)
		self.layout = QVBoxLayout()
		self.mainC.setLayout(self.layout)

		self.timeLabel = QLabel("Time", alignment=Qt.AlignCenter)
		self.timeLabel.setFixedSize(100, 43)
		self.timeLabel.setStyleSheet("Background:#225560; padding-left:20px; padding-right:20px;")

		self.gameTitleLabel = QLabel("Guessing Game :)", alignment=Qt.AlignCenter)
		self.gameTitleLabel.setFixedSize(253, 62)
		self.gameTitleLabel.setStyleSheet("background:#171219; border-radius:20px; padding-left:15px; color: white")

	def login_ui(self):
		self.basic_ui()
		self.username = QLineEdit()
		self.username.setPlaceholderText("Username")
		self.username.setMaxLength(25)
		self.username.setTextMargins(10, 10, 10, 10)
		self.username.setStyleSheet("background:#D3D3D3")

		self.passwordL = QLineEdit()
		self.passwordL.setPlaceholderText("Password")
		self.passwordL.setTextMargins(10, 10, 10, 10)
		self.passwordL.setStyleSheet("background:#D3D3D3")
		self.passwordL.setEchoMode(QLineEdit.EchoMode.Password)

		self.loginLabel = QPushButton("LOGIN")
		self.loginLabel.setFixedSize(152, 46)
		self.loginLabel.setStyleSheet("background:#8A997A; color:red")
		self.loginLabel.clicked.connect(self.loginCheck)

		#Sign in Tag
		self.signInTagInLogin = QPushButton("Sign in")
		self.signInTagInLogin.setFixedSize(152, 30)
		self.signInTagInLogin.setContentsMargins(0, 0, 0, 0)
		self.signInTagInLogin.setStyleSheet("background:#225560; color:blue; margin-top:-5px")
		self.signInTagInLogin.setFlat(True)
		self.signInTagInLogin.clicked.connect(self.runSingIn_ui)

		# add label to the window
		self.layout.addWidget(self.timeLabel, alignment= Qt.AlignRight)
		self.layout.addWidget(self.gameTitleLabel, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.username, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.passwordL, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.loginLabel, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.signInTagInLogin, alignment=Qt.AlignJustify)

	def sign_ui(self):
		self.basic_ui()
		self.username = QLineEdit()
		self.username.setPlaceholderText("Username")
		self.username.setMaxLength(25)
		self.username.setTextMargins(10, 10, 10, 10)
		self.username.setStyleSheet("background:#D3D3D3")

		self.passwordL2 = QLineEdit()
		self.passwordL2.setPlaceholderText("Confirm Password")
		self.passwordL2.setTextMargins(10, 10, 10, 10)
		self.passwordL2.setStyleSheet("background:#D3D3D3")
		self.passwordL2.setEchoMode(QLineEdit.EchoMode.Password)

		self.loginLabel = QPushButton("Sign In")
		self.loginLabel.setFixedSize(152, 46)
		self.loginLabel.setStyleSheet("background:#8A997A; color:red")
		self.loginLabel.clicked.connect(self.createUserCheck)

		#Login tag
		self.loginTagInSignIn = QPushButton("LogIn")
		self.loginTagInSignIn.setFixedSize(152, 46)
		self.loginTagInSignIn.setStyleSheet("background:#225560; color:blue")
		self.loginTagInSignIn.setFlat(True)
		self.loginTagInSignIn.clicked.connect(self.runLogin_ui)

		# add label to the window
		self.layout.addWidget(self.timeLabel, alignment= Qt.AlignRight)
		self.layout.addWidget(self.gameTitleLabel, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.username, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.passwordL, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.passwordL2, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.loginLabel, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.loginTagInSignIn, alignment=Qt.AlignJustify)

	def runLogin_ui(self):
		self.login_ui()

	def runSingIn_ui(self):
		self.sign_ui()

	def loginCheck(self):
		user = self.username.text()
		passW = self.passwordL.text()
		isAccessGrant = authorizeAccess(user, passW)
		if isAccessGrant:
			self.gameTitleLabel.setText(random.choice(game))
		else:
			self.gameTitleLabel.setText("Wrong username or password. Try again:)")

	def createUserCheck(self):
		pass

	def labelchange(self):

		pass

	


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screen = Window()
    screen.show()

    sys.exit(app.exec_())
		
		



		
