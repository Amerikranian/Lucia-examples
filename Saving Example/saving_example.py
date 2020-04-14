#Originally created by Ambro86
#Slight edits from Amerikranian
#This file demonstrates how to save data with Lucia
#No game window will be shown, the program will run, save an object to a file, print that saving was successful, and then exit.
#Necessary imports
from lucia import data
import pickle
#Create a quick class for saving
class Player:
	def __init__ (self, x, y):
		self.x= x
		self.y= y

def main():
	#Instantiate the player class
	player1 = Player(3, 5)
	#The key for encrypting data
	key = "KeyKeyKeyKey123123123"
	c= pickle.dumps(player1)
	c=data.compress(c)
	c= data.encrypt(c, key)
	with open("save.dat","wb") as f:
		f.write(c)
	print("Saved!")

#Run this via command line
if __name__ == "__main__":
	main()