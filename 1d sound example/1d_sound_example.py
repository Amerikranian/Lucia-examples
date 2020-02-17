#This file demonstrates how to play a simple file on a 1d grid with lucia
#The program will allow the user to press left and right arrow keys and simulate the sound moving towards or away from them as they move
#In addition, the program will also allow for the listener to press c to check their x coordinate
#imports
import lucia
import sys
#Create a quick class for the player
class player:
	def __init__(self):
		self._x = 0

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

#Call init in lucia
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
#Create a sound pool
#Must be done after lucia is initialized, otherwise the engine will throw a fit
sound_pool = lucia.audio_backend.SoundPool()
def main():
	#Show window
	lucia.show_window("1d sound example.")
	#Create the player
	listener = player()
	#Play a sound on a 1d grid.
	#Must use 2d playing function in order for the sound to actually pan
	sound_pool.play_2d("ding.ogg", listener.x, 0, 0, 0, True)
	while 1:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Check for key presses
		if lucia.key_pressed(lucia.K_LEFT):
			#Move the player 1 step to the left
			listener.x -= 1
			#Update the sound pool with the new player position
			sound_pool.update_listener_1d(listener.x)
		elif lucia.key_pressed(lucia.K_RIGHT):
			#Move the player 1 step to the right
			listener.x += 1
			#Update the sound pool with the new player position
			sound_pool.update_listener_1d(listener.x)
		elif lucia.key_pressed(lucia.K_c):
			#Output x coordinate
			lucia.output.output(str(listener.x))
		elif lucia.key_pressed(lucia.K_ESCAPE):
			#Exit
			lucia.quit()
			sys.exit()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)

#Run this via command line
if __name__ == "__main__":
	main()