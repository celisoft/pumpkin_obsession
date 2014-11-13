# -*- coding: utf-8 -*-

import random
import pygame
from utils import ImageLoader
from ground import Ground

class Pumpkin(pygame.sprite.Sprite):
	tile_size = 64
	
	def __init__(self, surface, left=None, difficulty=1):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface

		self.image = ImageLoader.get_single_sprite("SPRITE_PUMPKIN")
		
		self.move_width = self.surface.get_width() / self.tile_size
		self.move_height = self.surface.get_height() / self.tile_size * 0.75	

		self.rect = self.image.get_rect()
		if left is None:
			self.rect.left = random.randint(1, self.move_width-1) * self.tile_size
		else:
			self.rect.left = left * self.tile_size
			
		self.group = pygame.sprite.GroupSingle(self)

		self.move_difficulty = difficulty

	def get_tilesize(self):
		""" Return the tile size """
		return self.tile_size

	def move(self):
		""" Move pumpkin down """
		self.rect.top += self.move_height * self.move_difficulty
		
	def draw(self):
		""" Draw the pumpkin object """
		self.group.draw(self.surface)


class PumpkinManager():
	def __init__(self, surface):
		self.surface = surface
		self.pumpkins = pygame.sprite.LayeredUpdates()
		self.difficulty = 1

	def generate_pumpkin(self):
		""" Generate a pumpkin object and add it to pumpkin list """
		lPumpkin = Pumpkin(self.surface, None, self.difficulty)
		self.pumpkins.add(lPumpkin)

	def move_and_draw(self):
		""" Move pumpkin down and draw all pumpkins """
		for lPumpkin in self.pumpkins.sprites():
			lPumpkin.move()
		self.pumpkins.draw(self.surface)

	def increase_pumpkin_speed(self, player_level):
		""" Increase the pumpkins speed """
		self.difficulty = 1 + 0.25 * player_level

	def collide_with_player(self, player):
		""" Check if player sprite is in collision with a pumpkin one and update the score if necessary """
		lPlayerGroup = player.get_sprite_group()

		#check if there is a collision between sprites, automatically remove collided pumpkin
		collide = pygame.sprite.groupcollide(lPlayerGroup, self.pumpkins, False, True)

		#update the player score if necessary
		if len(collide) > 0:
			return True
		else:
			return False

	def collide_with_ground(self, ground):
		""" Check if player sprite is in collision with a pumpkin one and update the score if necessary """
		lGround = ground.get_sprite_group()

		#check if there is a collision between sprites, automatically remove collided pumpkin
		collide = pygame.sprite.groupcollide(lGround, self.pumpkins, False, True)

		#if there is collision, end game !!
		if len(collide) > 0:
			return True
		else:
			return False
		