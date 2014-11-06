# -*- coding: utf-8 -*-

import pygame
from utils import PlayerSpriteSheet

class Player(pygame.sprite.Sprite):
	PLAYER_RIGHT_1 = 0
	PLAYER_RIGHT_2 = 1
	PLAYER_RIGHT_STOP = 2
	PLAYER_FACE = 3
	PLAYER_BOTTOM = 4
	PLAYER_LEFT_1 = 5
	PLAYER_LEFT_2 = 6
	PLAYER_LEFT_STOP = 7
	
	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface
		self.spritesheet = PlayerSpriteSheet("SHEET_PLAYER")
		self.sprites = self.spritesheet.split()
		self.move_width = surface.get_width() / self.spritesheet.square_size
		self.move_height = surface.get_height() / self.spritesheet.square_size
		
		self.setSprite()
		
		self.level = 1
		self.score = 0

	def setSprite(self, code=None):
		if code is None:
			self.current_sprite = self.PLAYER_FACE
			self.image = self.sprites[self.PLAYER_FACE]
			self.rect = self.image.get_rect()
			self.rect.top = self.surface.get_height() - self.spritesheet.square_size
			self.group = pygame.sprite.GroupSingle(self)
		else:
			self.current_sprite = code
			self.image = self.sprites[code]

	def moveRight(self):
		if self.current_sprite in [self.PLAYER_FACE , self.PLAYER_BOTTOM, self.PLAYER_RIGHT_2]:
			self.setSprite(self.PLAYER_RIGHT_1)
		else:
			self.setSprite(self.PLAYER_RIGHT_2)
		self.rect.right += self.spritesheet.square_size

	def moveLeft(self):
		if self.current_sprite in [self.PLAYER_FACE , self.PLAYER_BOTTOM, self.PLAYER_LEFT_2]:
			self.setSprite(self.PLAYER_LEFT_1)
		else:
			self.setSprite(self.PLAYER_LEFT_2)
		self.rect.right -= self.spritesheet.square_size

	def stay(self):
		if self.current_sprite in [self.PLAYER_RIGHT_1, self.PLAYER_RIGHT_2]:
			self.setSprite(self.PLAYER_RIGHT_STOP)
		elif self.current_sprite in [self.PLAYER_LEFT_1, self.PLAYER_LEFT_2]:
			self.setSprite(self.PLAYER_LEFT_STOP)
		
	def draw(self):
		self.group.draw(self.surface)
