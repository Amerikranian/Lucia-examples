#Originally created by Ambro86
#Slight edits from Amerikranian
#This file demonstrates how to load data with Lucia
#No game window will be shown, the program will run, load an object to a file, demonstrate that the loading happened successfully, and then exit.
#Necessary imports
from lucia import data
import pickle
import sys
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
	#Read data from file
	with open("save.dat","rb") as f:
		save_data = f.read()
	#Decrypt and load data
	#Handle any errors that may occur. If loading fails, the program will exit
	try:
		save_data = data.decrypt(save_data, key)
		save_data = data.decompress(save_data)
		player1 = pickle.loads(save_data)
	except:
		print("Invalid save file")
		sys.exit()
	#Demonstrate that the object has been loaded successfully
	print("The player is at " + str(player1.x) + ", " + str(player1.y))

#Run this via command line
if __name__ == "__main__":
	main()