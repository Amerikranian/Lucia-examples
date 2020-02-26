#This program demonstrates how to use timers in lucia
#The program will output 2 messages spaced apart by 2 seconds and then exit
import lucia
import lucia.utils
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
def main():
	#Create a game window
	lucia.show_window("Timer Example.")
	#Create a timer
	countdown_timer = lucia.utils.timer.Timer()
	#Loop for 2 seconds
	while countdown_timer.elapsed <= 2000:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)
	#Output a message
	lucia.output.output("Now you see me...")
	#Restart the timer before continuing to loop
	countdown_timer.restart()
	#Loop for another 2 seconds
	while countdown_timer.elapsed <= 2000:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)
	#Output another message
	lucia.output.output("Now you don't!")
	lucia.quit()
	sys.exit()

#Run this via command line
if __name__ == "__main__":
	main()