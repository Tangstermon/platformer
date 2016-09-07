import pygame
import math
from Player import *
import random
from settings import *

vec = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,50))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect() 
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		
		#self.pos = vec(self.ran,self.ran)
		self.mov = vec(0,0)
		self.speed = 2

	def update(self):
		#print(Player().getPlayerPos())
		pass
	def moveTowardsPlayer(self, playerPos, enemy):
		enemy.mov = playerPos - enemy.pos
		dist = math.hypot(enemy.mov.x, enemy.mov.y)
		if dist < 0.1:
			dist = 1
		else:
			enemy.mov.x, enemy.mov.y = enemy.mov.x / dist, enemy.mov.y /dist	
		enemy.pos += enemy.mov * 2
		enemy.rect.center = enemy.pos