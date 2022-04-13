# User interface of interactions

from ctypes import alignment
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor

import sys, os, random

# my module
from authentication import *
from databases import getRandomWord


game =["Let's have fun ...", "Let's relax ...", "Let's play ..."]

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.signIn = False

		self.setWindowTitle("Guessing Word Game :)" )
		self.setFixedSize(410, 610)
		self.setStyleSheet("background:#225560")
		# self.login_ui()
		self.game_ui("Dove")

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

	def game_ui(self, username):
		self.mainC = QWidget()
		self.setCentralWidget(self.mainC)
		self.layout = QVBoxLayout()
		self.userAndTimelayout = QHBoxLayout()
		self.wordLetterLayout = QHBoxLayout()
		self.layout.addLayout(self.userAndTimelayout)
		self.userAndTimelayout.setStretch(0, 0)
		self.mainC.setLayout(self.layout)

		self.usernameLabel = QLabel(username, alignment=Qt.AlignCenter)
		self.usernameLabel.setFixedSize(100, 43)
		self.usernameLabel.setStyleSheet("Background:#A3A798; padding-left:20px; padding-right:20px;")

		self.timeLabel = QLabel("Time", alignment=Qt.AlignCenter)
		self.timeLabel.setFixedSize(100, 43)
		self.timeLabel.setStyleSheet("Background:#A3A798; padding-left:20px; padding-right:20px;")

		self.logOutTag = QPushButton("Log out")
		self.logOutTag.setFixedSize(152, 46)
		self.logOutTag.setStyleSheet("background:#225560; color:blue")
		self.logOutTag.setFlat(True)
		self.logOutTag.clicked.connect(self.runLogout_ui)

		self.gameTitleLabel = QLabel(random.choice(game), alignment=Qt.AlignCenter)
		self.gameTitleLabel.setFixedSize(253, 62)
		self.gameTitleLabel.setStyleSheet("background:#171219; border-radius:20px; padding-left:15px; color: white")

		self.startGame = QPushButton("Press to start")
		self.startGame.setFixedSize(152, 46)
		self.startGame.setStyleSheet("background:#70e000")
		self.startGame.clicked.connect(self.getWord)
		

		self.wordField = QLineEdit()
		self.wordField.setReadOnly(True)
		self.wordField.setBaseSize(80, 50)
		# self.wordField.setMaximumHeight(50)
		self.wordField.setPlaceholderText("_______")
		self.wordField.setMaxLength(25)
		self.wordField.setTextMargins(0, 10, 0, 10)
		self.wordField.setStyleSheet("background:#D3D3D3; font-size:30px")

		self.wordLabel = QLabel("Type a letter: ", alignment=Qt.AlignCenter)
		self.wordLabel.setFixedSize(120, 50)
		self.wordLabel.setStyleSheet("background:#A3A798; border-radius:20px; padding-left:15px;")

		self.yourLetter = QLineEdit()
		self.yourLetter.setPlaceholderText("_")
		self.yourLetter.setMaxLength(1)
		self.yourLetter.setFixedSize(80,50)
		self.yourLetter.setTextMargins(20, 10, 20, 10)
		self.yourLetter.setStyleSheet("background:#D3D3D3")

		self.checkLetter = QPushButton("Check")
		self.checkLetter.setFixedSize(80, 50)
		self.checkLetter.setStyleSheet("background:#225560; color:blue")
		self.checkLetter.clicked.connect(self.letterChecker)

		self.layout.addWidget(self.gameTitleLabel, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.startGame, alignment=Qt.AlignJustify)
		self.layout.addWidget(self.wordField, alignment=Qt.AlignJustify)
		self.layout.addLayout(self.wordLetterLayout)
		self.wordLetterLayout.addWidget(self.wordLabel)
		self.wordLetterLayout.addWidget(self.yourLetter)
		self.wordLetterLayout.addWidget(self.checkLetter)
		

		self.userAndTimelayout.addWidget(self.usernameLabel)
		self.userAndTimelayout.addWidget(self.timeLabel)

		self.layout.addWidget(self.logOutTag, alignment=Qt.AlignRight)

	def runLogin_ui(self):
		self.login_ui()

	def runSingIn_ui(self):
		self.sign_ui()

	def runLogout_ui(self):
		self.login_ui()

	def loginCheck(self):
		user = self.username.text()
		passW = self.passwordL.text()
		isAccessGrant = authorizeAccess(user, passW)
		if isAccessGrant[1]:
			self.game_ui(isAccessGrant[0])
			# self.gameTitleLabel.setText(random.choice(game))
		else:
			self.gameTitleLabel.setText("Wrong username or password. Try again:)")

	def createUserCheck(self):
		pass
	
	def getWord(self):
		self.word = getRandomWord()
		self.placeHoldForWord = ['__' for i in self.word]

		self.startGame.setText("Press to get Word")

	def letterChecker(self):
		letter = self.yourLetter.text().lower()
		word = self.word.lower()

		cloneWord = list(word)

		if letter in cloneWord:
			letterPosition = cloneWord.index(letter)
			cloneWord[letterPosition] = "+"
			self.placeHoldForWord[letterPosition] = letter
		elif letter=="!":
			pass


		self.wordField.setText(".".join(self.placeHoldForWord))

		if "".join(self.placeHoldForWord)==word:
			self.gameTitleLabel.setText("CONGRATULATION !!")

	


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screen = Window()
    screen.show()

    sys.exit(app.exec_())
		