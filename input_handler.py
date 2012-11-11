import sfml as sf
from collections import defaultdict

class Input():

	def __init__(self):
		self.keys_down = defaultdict(bool)
		self.keys_pressed = defaultdict(bool)

	def consumeEvent(self, event):
		self._cleanup_lists()

		if event.type == sf.Event.KEY_PRESSED:
			self._keyDown(event)
			return True

		if event.typ9e == sf.Event.KEY_RELEASED:
			self._keyUp(event)
			return True

		return False

	def keyDown(self, key):
		return self.keys_down[key]

	def keyPressed(self, key):
		return self.keys_pressed[key]

	def _keyDown(self, event):
		self.keys_down[event.code] = True

	def _keyUp(self, event):
		self.keys_down[event.code] = False
		self.keys_pressed[event.code] = True

	# this might be a heavy operation. if it becomes a problem then it will be looked at
	def _cleanupEvents(self):
		self.keys_pressed = defaultdict(bool)