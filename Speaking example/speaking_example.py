#This file demonstrates how to output text using Lucia
#The program will output a message whenever the user presses space and quit whenever they press enter
#imports
import lucia
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
def main():
	#Show window
	lucia.show_window("Speaking Example.")
	while 1:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Check for key presses
		if lucia.key_pressed(lucia.K_SPACE):
			lucia.output.output("Hello, world!")
		if lucia.key_pressed(lucia.K_RETURN):
			lucia.output.output("Good bye, world!")
			#Account for slower screen readers
			lucia.pygame.time.wait(1500)
			lucia.quit()
			sys.exit()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)

#Run this via command line
if __name__ == "__main__":
	main()