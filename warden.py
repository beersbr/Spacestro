import os
from config_handler import *

CONFIG_PATH_DIR = "resources/config/"

GAMESTATE_PLAYING = 0
GAMESTATE_PAUSED = 1
GAMESTATE_MENU1 = 2

def getConfigFilePath(name):
	filename = name+".json"
	path = os.path.join(CONFIG_PATH_DIR, name)

	if os.path.exists(path):
		return path

	return ""

class Warden():
	def __init__(self):
		self.state = GAMESTATE_MENU1
		self.window = None
		self.config = None

	def initialize(self, config):
		self.config = Configuration(getConfigFilePath("game"))
		self.window = sf.RenderWindow(self.config["window_size"], self.config["window_title"])
		self.window.frame_rate_limit = self.config["framerate"]
		
