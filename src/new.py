import pygame
import math
import random
from Camera import Camera
from Sprite import *
from os import path
from TileMap import *
#from Collisions import *

from settings import *

class Game:

	def __init__(self):
		pygame.init()
		self.mainClock = pygame.time.Clock()
		self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Game")

		dirC = path.dirname(__file__)
		img_dir = path.join(path.dirname(__file__), "..\img")

		self.level = TileMap(path.join(dirC, 'level1.txt'))
		self.enemySprite = pygame.image.load(path.join(img_dir, "poulpi.png")).convert()
		self.spriteSheet = SpriteSheet(path.join(img_dir, 'spritesheet_tiles.png'))
		self.playerSprite = pygame.image.load(path.join(img_dir, "knight.png")).convert()
		
		self.avg = 0
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.wall_sprites = pygame.sprite.Group()
		self.ground_sprites = pygame.sprite.Group()

		self.load() 

	def draw_grid(self):
		for x in range(0, WINDOW_WIDTH, TILESIZE):
			pygame.draw.line(self.surface, LIGHTGREY, (x,0), (x, WINDOW_HEIGHT))
		for y in range(0, WINDOW_HEIGHT, TILESIZE):
			pygame.draw.line(self.surface, LIGHTGREY, (0,y), (WINDOW_WIDTH, y))
	
	def draw_text(self, surf, text, size, x, y):
	    font_name = pygame.font.match_font("arial")
	    font = pygame.font.Font(font_name, size)
	    text_surface = font.render(text, True, BLACK)
	    text_rect = text_surface.get_rect()
	    text_rect.midtop = (x, y)	
	    surf.blit(text_surface, text_rect)

	def load(self):
		for row, tiles in enumerate(self.level.level_data):
			for col, tile in enumerate(tiles):
				# ground = Ground(col, row, self)
				# self.ground_sprites.add(ground)
				# self.all_sprites.add(ground)
				if tile == 'P':
					self.player = Player(col, row, self)
					self.all_sprites.add(self.player)
				if tile == '1':
					wall = Wall(col, row, self)
					self.all_sprites.add(wall)
					self.wall_sprites.add(wall)
				if tile == '*':
					wall = Wall(col, row, self)
					self.all_sprites.add(wall)
					self.wall_sprites.add(wall)
				if tile == 'M':
					enemy = Enemy(col, row,self)
					self.all_sprites.add(enemy)

		self.camera = Camera(self.player, WINDOW_WIDTH, WINDOW_HEIGHT, 
						self.level.width, self.level.height)

		self.all_sprites.add(self.player)
		counter = 0
		total = 0
	
	def run(self):
	
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False		

			self.camera.moveWorld(self.player)
			self.surface.fill(WHITE)
			self.mainClock.tick(FPS)
			self.all_sprites.update()
			for a in self.all_sprites:
				if a.rect.colliderect(self.camera.screenRect):
					self.surface.blit(a.image, [(a.rect.x - self.camera.screenRect.x),
											(a.rect.y - self.camera.screenRect.y)])

			currFPS = self.mainClock.get_fps()
			self.draw_text(self.surface, str(currFPS), 18, 550, 100)
			pygame.display.flip()

game = Game()

game.run()
print(game.avg)
pygame.quit()