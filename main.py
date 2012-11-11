import sfml as sf
from config_handler import *
from warden import *


# def main():
# 	window = sf.RenderWindow(sf.VideoMode(800, 600), "Test Window")
# 	window.framerate_limit = 60

# 	running = True

# 	while running:
# 		for event in window.iter_events():
# 			if event.type == sf.Event.CLOSED:
# 				running = False

# 			if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
# 				running = False

# 		window.clear(sf.Color.BLACK)
# 		window.display()

# 	window.close()

# if __name__ == '__main__':
# 	main()