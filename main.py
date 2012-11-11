import sfml as sf
from config_handler import *
from warden import *

class Game():
	def __init__(self):
		self.warden = Warden()

	def setup(self):
		self.warden.initialize("game")

	def run(self):

		while self.warden.state != GAMESTATE_QUIT:
			for event in self.warden.window.iter_events():
				self.warden.consumeEvent(event)

			if self.warden.input.keyDown(sf.Keyboard.ESCAPE):
				self.warden.state = GAMESTATE_QUIT

			self.warden.window.clear(sf.Color(255, 0, 255))
			self.warden.window.display()

	def cleanup(self):
		pass

if __name__ == '__main__':
	game = Game()
	game.setup()
	game.run()