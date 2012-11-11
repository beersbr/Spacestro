import os
from config_handler import *
from input_handler import *

CONFIG_PATH_DIR = "./resources/config/"

GAMESTATE_QUIT = -1
GAMESTATE_PLAYING = 0
GAMESTATE_PAUSED = 1
GAMESTATE_MENU1 = 2

class Warden():
	def __init__(self):
		self.state = GAMESTATE_MENU1
		self.window = None
		self.config = None
		self.input = None

	def initialize(self, config):
		self.config = Configuration(config)
		self.window = sf.RenderWindow(sf.VideoMode(self.config["window_size"][0], self.config["window_size"][1]), self.config["window_title"])
		self.window.framerate_limit = self.config["framerate"]

		self.input = Input()

	def consumeEvent(self, event):
		if event.type == sf.Event.CLOSED:
			self.state = GAMESTATE_QUIT
			return GAMESTATE_QUIT

		self.input.consumeEvent(event)

		return event.type