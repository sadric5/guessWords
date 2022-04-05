import re
from databases import wordFind

def main(word):
	print("Let's start our guessing Letter Game :)\n")
	lengthWord = len(word)

	placeHoldForWord = ['__' for i in word]


	checker = True #make sure we are not lock in endless loop
	cloneWord = list(word)
	while checker:

		userLetter = input("Enter Your Letter:")


		if userLetter in cloneWord:
			letterPosition = cloneWord.index(userLetter)
			cloneWord[letterPosition] = "+"
			placeHoldForWord[letterPosition] = userLetter
		elif userLetter=="!":
			break




		print(".".join(placeHoldForWord))

		if "".join(placeHoldForWord)==word:
			print("Congratulation !!!")
			break





if __name__ == '__main__':

	main(wordFind())