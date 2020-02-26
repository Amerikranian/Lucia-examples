#This file demonstrates how to play a simple file on a 2d grid with lucia
#The program will allow the user to press left, down, right, and up arrow keys and simulate the sound moving towards or away from them as they move
#In addition, the program will also allow for the listener to press c to check their x coordinate
#imports
import lucia
import sys
#Create a quick class for the player
class player:
	def __init__(self):
		self._x = 0
		self._y = 0

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		self._y = value

#Call init in lucia
#Must be called in order for lucia to work properly
#Since we are using bass, I will just call init without the open Al parameter.
#Should you wish to change it, the desired param is in __init__.py in Lucia's directory
lucia.initialize()
#Create a sound pool
#Must be done after lucia is initialized, otherwise the engine will throw a fit
sound_pool = lucia.audio_backend.SoundPool()
#Create a moving function to simplify updating of sounds
def move_object(obj, value):
	#From lowest to highest, the values are 0, 1, 2, or 3 moving the object forward, right, backward, and left respectively.
	if value == 0: obj.y += 1
	elif value == 1: obj.x += 1
	elif value == 2: obj.y -= 1
	elif value == 3: obj.x -= 1
	#Update listener after all is said and done
	sound_pool.update_listener_2d(obj.x, obj.y)

def main():
	#Show window
	lucia.show_window("2d Sound Example.")
	#Create the player
	listener = player()
	#Play a sound on a 2d grid.
	sound_pool.play_2d("ding.ogg", listener.x, listener.y, 0, 0, True)
	while 1:
		#Allow lucia to update it's internal queues and events
		lucia.process_events()
		#Check for key presses
		if lucia.key_pressed(lucia.K_LEFT):
			#Move the player 1 step to the left
			move_object(listener, 3)
		elif lucia.key_pressed(lucia.K_RIGHT):
			#Move the player 1 step to the right
			move_object(listener, 1)
		elif lucia.key_pressed(lucia.K_UP):
			#Move the player one step forward
			move_object(listener, 0)
		elif lucia.key_pressed(lucia.K_DOWN):
			#Move the player one step backwards
			move_object(listener, 2)
		elif lucia.key_pressed(lucia.K_c):
			#Output coordinates
			lucia.output.output(str(listener.x) + ", " + str(listener.y))
		elif lucia.key_pressed(lucia.K_ESCAPE):
			#Exit
			lucia.quit()
			sys.exit()
		#Sleep for 2 milliseconds
		lucia.pygame.time.wait(2)

#Run this via command line
if __name__ == "__main__":
	main()