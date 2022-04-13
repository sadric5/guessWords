# Return random words based on the user desired field
from mysql import connector
from credential import *
import hashlib, random

#connect To The Database
my_db = connector.connect (
    	user = USERNAME,
    	password = PASSWORD,
    	host = HOST,
    	database = DATABASE
	)

mycursor = my_db.cursor()

def authenticateUser(username='', password=''):

	# Only the hash value of the password was stored
	password = hashlib.sha512(password.encode()).hexdigest()
	sql = """ SELECT * FROM account WHERE username="{}" AND passwords="{}" """.format(username, password)
	
	mycursor.execute(sql)
	data = mycursor.fetchall()
	
	if data:
		return True
	else:
		return False


def createUser(username, password):
	# Store only the hash value of the password.
	password = hashlib.sha512(password.encode()).hexdigest()
	sql = """ INSERT INTO account (username, passwords) values ("{}", "{}") """.format(username, password)
	mycursor.execute(sql)
	my_db.commit()

def getRandomWord():
	wordId = random.randint(1, 2)
	
	sql = """ SELECT word FROM dictionary WHERE id={} """.format(wordId)
	mycursor.execute(sql)
	data = mycursor.fetchone()
	return data[0]


if __name__ == "__main__":	
	# createUser("Dove", "Kent")
	print(getRandomWord())




	