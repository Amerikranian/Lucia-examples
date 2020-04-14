#This program demonstrates how to use virtual input in Lucia
#The program will prompt the user to type in a message and will print it to the screen before exiting
import lucia
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
def main():
	#Create a game window
	lucia.show_window("Input Example.")
	#Create the virtualInput object. See the module itself for further details
	input_handler = lucia.ui.virtualinput.virtualInput()
	#Gather our user input.
	user_response = input_handler.run("Please enter something!")
	#Output our response
	print(user_response)
	#Properly quit
	lucia.quit()
	sys.exit()

#Run this via command line
if __name__ == "__main__":
	main()