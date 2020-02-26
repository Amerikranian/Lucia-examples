#This file demonstrates how to use Lucia's keyboard functions
#imports
import lucia
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
def main():
	#Show window
	lucia.show_window("Lucia keyboard example.")
	while 1:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Check for key presses
		#Typically this should be done in a separate function, but we will keep this as simple as possible
		if lucia.key_pressed(lucia.K_SPACE):
			print("You pressed space!")
			sys.exit()
		#Check for key holds
		if lucia.key_down(lucia.K_RETURN):
			print("You held enter!")
			lucia.quit()
			sys.exit()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)

#Run this via command line
if __name__ == "__main__":
	main()