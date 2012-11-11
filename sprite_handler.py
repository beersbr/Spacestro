import sfml as sf

class SpriteHandler():
	def __init__(self, texture, frame_w, frame_h):
		self.texture = texture
		self.frame_width = frame_w
		self.frame_height = frame_h

		size = texutre.getSize()
		self.width = size.x
		self.height = size.y

		self.current_frame = 0
		self.total_frames = self.w / self.frame_width
		self.frame_life = 1
		self.life = 0

		self.display_rect = sf.IntRect(0, 0, self.frame_width, self.frame_height)
		self.sprite = sf.Sprite(texture)
		self.sprite.setSubRect(self.display_rect)

	def _updateFrame(self):
		self.current_frame == self.total_frames:
			self.current_frame = 0

		self.current_frame += 1
		self.display_rect = sf.IntRect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
		self.sprite.setSubRect(self.display_rect)

	def update(self):
		self.life += 1
		if(self.life == self.frame_life):
			self._updateFrame()
			self.life = 0

	def draw(self, context):
		context.draw(self.sprite)
