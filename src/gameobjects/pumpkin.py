# -*- coding: utf-8 -*-

import random
import pygame
from utils import ImageLoader

class Pumpkin(pygame.sprite.Sprite):
	tile_size = 64
	
	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface

		self.image = ImageLoader.get_single_sprite("SPRITE_PUMPKIN")
		
		self.move_width = self.surface.get_width() / self.tile_size
		self.move_height = self.surface.get_height() / self.tile_size * 0.75
		
		self.rect = self.image.get_rect()
		self.rect.left = random.randint(0, self.move_width-1) * self.tile_size

		self.group = pygame.sprite.GroupSingle(self)		

	def move(self):
		""" Move pumpkin down """
		self.rect.top += self.move_height
		
	def draw(self):
		""" Draw the pumpkin object """
		self.group.draw(self.surface)


class PumpkinManager():
	def __init__(self, surface):
		self.surface = surface
		self.pumpkins = pygame.sprite.LayeredUpdates()

	def generate_pumpkin(self):
		""" Generate a pumpkin object and add it to pumpkin list """
		lPumpkin = Pumpkin(self.surface)
		self.pumpkins.add(lPumpkin)

	def move_and_draw(self):
		""" Move pumpkin down and draw all pumpkins """
		for lPumpkin in self.pumpkins.sprites():
			lPumpkin.move()
		self.pumpkins.draw(self.surface)

	def collide_with_player(self, player):
		""" Check if player sprite is in collision with a pumpkin one and update the score if necessary """
		lPlayerGroup = player.get_sprite_group()

		#check if there is a collision between sprites, automatically remove collided pumpkin
		collide = pygame.sprite.groupcollide(lPlayerGroup, self.pumpkins, False, True)

		#update the player score if necessary
		if len(collide) > 0:
			player.score_update()
		