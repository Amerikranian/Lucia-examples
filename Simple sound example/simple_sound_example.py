#This file demonstrates how to play a simple file with lucia
#The program will continuously play a sound and will quit upon the user pressing alt f4
#imports
import lucia
import sys
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
#Create a sound pool
#Must be done after lucia is initialized, otherwise the engine will throw a fit
sound_pool = lucia.audio_backend.SoundPool()
def main():
	#Show window
	lucia.show_window("Simple sound example.")
	#Play a stationary sound
	#Stationary means that the sound cannot move, regardless of what the player does
	#The first parameter is the filename, while the second one dictates whether the sound can loop or not
	sound_pool.play_stationary("ding.ogg", True)
	while 1:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)

#Run this via command line
if __name__ == "__main__":
	main()