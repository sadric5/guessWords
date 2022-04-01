def main(word):
	print("Let's start our guessing Game :)\n")
	lengthWord = len(word)

	placeHoldForWord = ['__' for i in word]
	print(".".join(placeHoldForWord))





if __name__ == '__main__':
	main("HELLO")