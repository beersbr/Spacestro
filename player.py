import entity
from sprite_handler import SpriteHandler
from config_handler import Configuration

class Player(entity.Entity):
	def __init__(self):
		entity.Entity.__init__(self)
		self.sprite = SpriteHandler()
		self.config = Configuration("player")

	def update(self, args):
		pass

	def draw(self, context):
		pass
