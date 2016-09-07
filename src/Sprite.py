import pygame 
import math
import random
from settings import *
vec = pygame.math.Vector2

def collide_with_walls(sprite, dir, wall_group):
		if dir == 'x':
			hits = pygame.sprite.spritecollide(sprite, wall_group, False)
			if hits:
				if sprite.vel.x >0:
					sprite.pos.x = hits[0].rect.left - sprite.rect.width
				if sprite.vel.x <0:
					sprite.pos.x = hits[0].rect.right
				sprite.vel.x = 0
				sprite.rect.x = sprite.pos.x
		if dir == 'y':
			hits = pygame.sprite.spritecollide(sprite, wall_group, False)
			if hits:
				if sprite.vel.y >0:
					sprite.pos.y = hits[0].rect.top - sprite.rect.height
				if sprite.vel.y <0:
					sprite.pos.y = hits[0].rect.bottom
				sprite.vel.y =0
				sprite.rect.y = sprite.pos.y

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self._layer = 2
		self.wall_group = game.wall_sprites
		self.image = pygame.transform.scale(self.game.playerSprite, (TILESIZE*2,TILESIZE*2))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.pos = vec(x,y) * TILESIZE
		
		self.right = False
		self.left = False
		self.up = False
		self.down = False


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
		collide_with_walls(self,'x', self.wall_group)
		self.rect.y = self.pos.y
		collide_with_walls(self,'y', self.wall_group)

		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, game):
		pygame.sprite.Sprite.__init__(self)
		self._layer = 1
		self.game = game
		self.wall_group = game.wall_sprites
		self.image = pygame.transform.scale(game.enemySprite, (TILESIZE*2,TILESIZE*2))
		self.rect = self.image.get_rect() 
		self.image.set_colorkey(BLACK)
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.pos = vec(x,y) * TILESIZE
		
		self.mov = vec(0,0)
		self.ran = random.uniform(1,2)
		self.speed = self.ran

		self.right = False
		self.left = False
		self.up = False
		self.down = False
		self.interval = 200
		self.start = pygame.time.get_ticks()
		self.poNe = random.randint(0,3)

		self.accSpeed = 0.1


	def update(self):
		
		finish = pygame.time.get_ticks()
		self.mov = self.game.player.pos - self.pos
		dist = math.hypot(self.mov.x, self.mov.y)
		if dist < 300:
			self.moveTowardsPlayer(self.game.player.pos)
		else:

			if self.poNe == 0:
				self.acc.x = -self.accSpeed
			if self.poNe == 1:
				self.acc.x = self.accSpeed
			if self.poNe == 2:
				self.acc.y = -self.accSpeed
			if self.poNe == 3:
				self.acc.y = self.accSpeed
			
			if finish - self.start >= self.interval:
				self.poNe = random.randint(0,3)
				self.start = finish

			self.acc *= 0.5
			self.vel += self.acc 
			self.pos += self.vel + 0.5 * self.acc
			self.pos.normalize()
			self.rect.x = self.pos.x
			collide_with_walls(self,'x', self.wall_group)
			self.rect.y = self.pos.y
			collide_with_walls(self,'y', self.wall_group)
			

	def moveTowardsPlayer(self, playerPos):
		self.vel = playerPos - self.pos
		dist = math.hypot(self.vel.x, self.vel.y)
		
		if dist < 0.1:
			dist = 1
		else:
			self.vel.x, self.vel.y = self.vel.x / dist, self.vel.y /dist	

		self.pos += self.vel * self.ran
		
		self.rect.x = self.pos.x
		collide_with_walls(self,'x', self.wall_group)
		self.rect.y = self.pos.y
		collide_with_walls(self,'y', self.wall_group)

class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.image = self.game.spriteSheet.get_image(0,0,128,128)
		self.rect = self.image.get_rect() 
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

class Ground(pygame.sprite.Sprite):
	def __init__(self, x, y, game):
		pygame.sprite.Sprite.__init__(self)
		self._layer = 0
		self.game = game
		self.image = self.game.spriteSheet.get_image(650,520,128,128)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect() 
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

class SpriteSheet:
	def __init__(self, filename):
		self.spriteSheet = pygame.image.load(filename).convert()

	def get_image(self, x, y, width, height):
		new_Width = width/4
		new_Height = height/4
		image = pygame.Surface((width, height))
		image.blit(self.spriteSheet,(0,0), (x, y, width, height))
		image = pygame.transform.scale(image,(int(new_Width), int(new_Height)))
		return image
