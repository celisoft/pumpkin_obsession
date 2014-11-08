# -*- coding: utf-8 -*-

import pygame
from utils import PlayerSpriteSheet

class Player(pygame.sprite.Sprite):
	PLAYER_RIGHT_1 = 0
	PLAYER_RIGHT_2 = 1
	PLAYER_RIGHT_STOP = 2
	PLAYER_FACE = 3
	PLAYER_BOTTOM_DOWN = 4
	PLAYER_BOTTOM_UP = 5
	PLAYER_LEFT_1 = 6
	PLAYER_LEFT_2 = 7
	PLAYER_LEFT_STOP = 8

	PLAYER_MOVE_STEP = 64
	
	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface
		self.spritesheet = PlayerSpriteSheet("SHEET_PLAYER")
		self.sprites = self.spritesheet.split()
		self.move_width = surface.get_width() / self.PLAYER_MOVE_STEP
		self.move_height = surface.get_height() / self.spritesheet.square_size
		
		self.set_sprite()
		self.score = 0

	def set_sprite(self, code=None):
		""" Set the sprite, if no code given, the skeleton is in front of us """
		if code is None:
			self.current_sprite = self.PLAYER_FACE
			self.image = self.sprites[self.PLAYER_FACE]
			self.rect = self.image.get_rect()
			self.rect.top = self.surface.get_height() - self.spritesheet.square_size
			self.group = pygame.sprite.GroupSingle(self)
		else:
			self.current_sprite = code
			self.image = self.sprites[code]

	def move_right(self):
		""" Go to the right with alternative sprite """
		if self.current_sprite in [self.PLAYER_FACE , self.PLAYER_BOTTOM_DOWN, self.PLAYER_RIGHT_2]:
			self.set_sprite(self.PLAYER_RIGHT_1)
		else:
			self.set_sprite(self.PLAYER_RIGHT_2)
		self.rect.right += self.PLAYER_MOVE_STEP

	def move_left(self):
		""" Go to the left with alternative sprite """
		if self.current_sprite in [self.PLAYER_FACE , self.PLAYER_BOTTOM_DOWN, self.PLAYER_LEFT_2]:
			self.set_sprite(self.PLAYER_LEFT_1)
		else:
			self.set_sprite(self.PLAYER_LEFT_2)
		self.rect.right -= self.PLAYER_MOVE_STEP

	def jump(self):
		""" Everybody jump so is our skeleton """
		self.set_sprite(self.PLAYER_BOTTOM_UP)
		self.rect.top -= (self.spritesheet.square_size * 0.75)
			
	def wait(self):
		""" Set the waiting position for the player """
		self.set_sprite(self.PLAYER_BOTTOM_DOWN)
		self.rect.top = self.surface.get_height() - self.spritesheet.square_size
		
	def draw(self):
		""" Draw the player sprite """
		self.group.draw(self.surface)
