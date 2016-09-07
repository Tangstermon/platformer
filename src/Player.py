import pygame 
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((TILESIZE,TILESIZE))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.pos = vec(x,y) * TILESIZE

	def update(self):
		
		self.acc = vec(0,0)
		keystate = pygame.key.get_pressed()
		
		if keystate[pygame.K_LEFT]:
			self.acc.x = -0.5
		if keystate[pygame.K_RIGHT]:
			self.acc.x = 0.5
		if keystate[pygame.K_UP]:
			self.acc.y = -0.5
		if keystate[pygame.K_DOWN]:
			self.acc.y = 0.5

		self.acc += self.vel * -0.1
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc
		self.pos.normalize()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y 

	def getPlayerPos(self):
		return self.pos