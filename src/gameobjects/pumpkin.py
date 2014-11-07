# -*- coding: utf-8 -*-

import random
import pygame
from utils import ImageLoader

class Pumpkin(pygame.sprite.Sprite):
	tile_size = 32
	
	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface

		self.image = ImageLoader.getSingleSprite("SPRITE_PUMPKIN")
		
		self.move_width = self.surface.get_width() / self.tile_size
		self.move_height = self.surface.get_height() / self.tile_size * 0.75
		
		self.rect = self.image.get_rect()
		self.rect.left = random.randint(0, self.move_width-1) * self.tile_size

		self.group = pygame.sprite.GroupSingle(self)		

	def move(self):
		self.rect.top += self.move_height

	def remove(self):
		raise NotImplemented
		
	def draw(self):
		self.group.draw(self.surface)
