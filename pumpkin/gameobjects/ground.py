# -*- coding: utf-8 -*-

import pygame
from utils import ImageLoader

class GroundSquare(pygame.sprite.Sprite):
	tile_size = 32
	
	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface

		self.image = ImageLoader.get_single_sprite("SPRITE_GROUND")
		self.move_width = self.surface.get_width() / self.tile_size

		self.rect = self.image.get_rect()
		self.rect.top = self.surface.get_height() - self.tile_size
		
		self.group = pygame.sprite.GroupSingle(self)	

	@classmethod
	def get_tile_size(self):
		""" Return the square tile size """
		return self.tile_size

	def set_left(self, value):
		""" Set the left rect value """
		self.rect.left += value * self.tile_size
		
	def draw(self):
		""" Draw the ground """
		self.squares.draw(self.surface)
	

class Ground():
	def __init__(self, surface):
		self.surface = surface
		self.ground_squares = pygame.sprite.LayeredUpdates()

		lSquareSize = GroundSquare.get_tile_size()
		lSquareQty = self.surface.get_width() / lSquareSize

		for i in range(lSquareQty):
			lSquare = GroundSquare(self.surface)
			lSquare.set_left(i)
			self.ground_squares.add(lSquare)

	def get_sprite_group(self):
		""" Return the squares group """
		return self.ground_squares

	def draw(self):
		""" Draw all ground squares """
		self.ground_squares.draw(self.surface)

		