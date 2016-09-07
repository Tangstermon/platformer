import pygame
from settings import *


class TileMap:
	def __init__(self, filename):
		self.level_data = []
		with open(filename, 'rt') as f:
			for line in f:
				self.level_data.append(line.strip())

		self.tilewidth = len(self.level_data[0])
		self.tileheight = len(self.level_data)
		self.width = self.tilewidth * TILESIZE
		self.height = self.tileheight * TILESIZE
