def id_gen():
	max_id = 1000000

	_id = 0
	while _id < max_id:
		yield _id
		_id += 1

	print "ERROR: Too many id's generated: "+max_id
	return None

class Entity():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.ax = 0
		self.ay = 0

		self.angle = 0.0

		self.id = id_gen()

	def update(self, args):
		return True

	def draw(self, context):
		return True