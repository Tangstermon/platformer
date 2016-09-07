import pygame
from settings import *

class Camera:

	def __init__(self, player, width, height, mWidth, mHeight):

		self.shift_x = 0
		self.shift_y = 0

		self.image = pygame.Surface((10,10))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		#self.rect.center = (self.viewBox_x,self.viewBox_y)
		self.rect.center = (10,10)
		self.offset = 1
		self.screenRect = pygame.Rect(0,0,WINDOW_WIDTH, WINDOW_HEIGHT)
		self.mapSize = pygame.Rect(0,0,mWidth,mHeight)

	def update(self, player):
		pass
	def moveWorld(self, player):
		self.screenRect.centerx = player.rect.centerx
		self.screenRect.centery = player.rect.centery
		#player moves right
		if self.screenRect.top<self.mapSize.top:
			self.screenRect.top=self.mapSize.top

		if self.screenRect.bottom > self.mapSize.bottom:
			self.screenRect.bottom = self.mapSize.bottom

		if self.screenRect.left < self.mapSize.left:
			self.screenRect.left = self.mapSize.left

		if self.screenRect.right > self.mapSize.right:
			self.screenRect.right = self.mapSize.right
			

