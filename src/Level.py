import pygame
from settings import *

class Camera:

	def __init__(self):

		self.shift_x = 0
		self.shift_y = 0

		self.viewBox_x = WINDOW_WIDTH/3
		self.viewBox_y = WINDOW_HEIGHT/3
		self.image = pygame.Surface((10,10))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		#self.rect.center = (self.viewBox_x,self.viewBox_y)
		self.rect.center = (10,10)
		self.offset = 1

	def update(self):
		pass
	def moveWorld(self, player, objectRect):
		#player moves right
		if player.pos.x  > self.viewBox_x:
			objectRect.rect.x = objectRect.rect.x - self.offset
		#player moves left
		if player.pos.x < self.viewBox_x:
			objectRect.rect.x = objectRect.rect.x + self.offset
		#player moves up
		if player.pos.y < self.viewBox_y:
			objectRect.rect.y = objectRect.rect.y - self.offset
		#player moves down
		if player.pos.y > self.viewBox_y:
			objectRect.rect.y = objectRect.rect.y + self.offset
		

