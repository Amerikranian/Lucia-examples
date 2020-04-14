#This program demonstrates how to use the basic menu module in Lucia
#The program will create a menu with multiple items before printing what the user has chosen
import lucia
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
def main():
	#Create a game window
	lucia.show_window("Basic Menu Example.")
	#Create a menu. This will not contain any sounds and will not be explain in great detail here, the module is commented extremely well for a change.
	menu_handler = lucia.ui.menu.Menu()
	#Add items
	menu_handler.add_item_tts("Start game")
	menu_handler.add_item_tts("Options")
	menu_handler.add_item_tts("Exit.")
	#Run the menu
	choice = menu_handler.run("Please select an item with your up and down arrow keys")
	#Output the user's choice
	print(choice)
	#Properly exit
	lucia.quit()
	sys.exit()

#Run this via command line
if __name__ == "__main__":
	main()