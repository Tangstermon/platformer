import pygame
import Enemy
import Player
import Wall

class Collisions:

	def __init__(self, sprite, spriteGroup):
		self.sprite = sprite
		self.spriteGroup = spriteGroup


	def collide(self):
		hits = pygame.spritecollide(self.sprite, spriteGroup, False)
		if hits:
			sprite.vel = (0,0)