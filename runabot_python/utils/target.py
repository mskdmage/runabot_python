import cv2

class Target(object):
	def __init__(self, ref):
		self.ref = ref
		self.image = self.load_image()

	def load_image(self):
		return cv2.imread(self.ref)