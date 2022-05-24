import cv2
import pyautogui
import numpy as np
from random import randint
from time import sleep

class Bot(object):
	def __init__(self, tolerance=.69, view_range=(0,0,2000,2000)):
		self.tolerance = tolerance
		self.view_range = view_range
		self.ref = './.peek/snap.png'

	def peek(self):
		pyautogui.screenshot(self.ref, self.view_range)
		snap = cv2.imread(self.ref)
		return snap

	def find(self, target):
		peek = self.peek()
		match = cv2.matchTemplate(peek, target, cv2.TM_CCOEFF_NORMED)
		match_coords = np.where(match > self.tolerance)

		if len(match_coords[0]) > 0:
			return (match_coords[1][0], match_coords[0][0])

	def mine(self, coords):
		pyautogui.moveTo(coords[0] + 40, coords[1] + 40, 0)
		pyautogui.click()
		sleep(randint(8, 10))