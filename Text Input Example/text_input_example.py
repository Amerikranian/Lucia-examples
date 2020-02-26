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
	#Create a virtual input object. the Parameters are message (what is to be spoken upon running the input), password (boolean) dictating if letters are hidden or not, whitelist (a list of allowed characters, see the module itself for more details), value, the initial value of the input string), callback (a function which will be called in the main loop should it be passt to the object), and hidden_message (the message which will be spoken if the password is set to True and the user types in a letter).
	input_handler = lucia.ui.virtualinput.VirtualInput("Please enter something!")
	#Gather our user input.
	user_response = input_handler.run()
	#Output our response
	print(user_response)
	#Properly quit
	lucia.quit()
	sys.exit()

#Run this via command line
if __name__ == "__main__":
	main()