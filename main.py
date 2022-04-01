import re

def main(word):
	print("Let's start our guessing Letter Game :)\n")
	lengthWord = len(word)

	placeHoldForWord = ['__' for i in word]

	checker = True
	cloneWord = list(word)
	while checker:

		userLetter = input("Enter Your Letter:")


		if userLetter in cloneWord:
			letterPosition = cloneWord.index(userLetter)
			cloneWord[letterPosition] = "+"
			placeHoldForWord[letterPosition] = userLetter
		elif userLetter=="!" or "".join(placeHoldForWord)==word:
			checker = False




		print(".".join(placeHoldForWord))





if __name__ == '__main__':
	main("HELLO")