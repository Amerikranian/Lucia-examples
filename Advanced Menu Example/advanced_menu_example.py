#Originally created by Ambro86
#Slight edits by Amerikranian
#This program demonstrates how to use a more advanced menu in Lucia
#The program will run, allow for the user to choose an item, and then exit

import lucia
import sys
from lucia.ui import menu2
lucia.initialize()

def main():
	#Window tytle
	test = lucia.show_window("Menu")
	#Now we insert the menu elements
	MenuItems= [
		menu2.MenuItem("start", can_return=True),
		menu2.MenuItem("options", can_return=True),
		menu2.MenuItem("information", can_return=True),
		menu2.MenuItem("exit", can_return=True),
	]
	#Now let's list the sounds of the menu
	#No sounds will play do to them not being provided with the example.
	#You can place items named scroll1.wav, enter1.wav, and border1.wav in the same directory as the script and the menu will react accordingly.
	menu1=menu2.Menu(items=MenuItems, clicksound="scroll1.wav", entersound="enter1.wav", edgesound="border1.wav", itempos=0, on_index_change=None)
	#We make the menu come out only when the user presses exit.
	while 1:
		result = menu1.run()
		if result[0]["name"] == "start":
			lucia.output.speak("Starting the game...")
		if result[0]["name"] == "information":
			lucia.output.speak("This is a test!")
		if result[0]["name"] == "options":
			lucia.output.speak("Here are the options!")
		if result[0]["name"] == "exit":
			lucia.output.speak("Thanks for playing!")
			lucia.quit()
			sys.exit()

#Run this via command line
if __name__ == "__main__":
	main()