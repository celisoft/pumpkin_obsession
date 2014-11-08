# -*- coding: utf-8 -*-

import pygame
from utils import ImageLoader
from pumpkin import Pumpkin

class ScoreArea():
	def __init__(self, surface, score=0):
		self.surface = surface

		self.pumpkin = Pumpkin(self.surface, 0.5)
		
		self.font = pygame.font.Font(None, 36)
		self.update_text(score)

	def update_text(self, score):
		""" Update the text content (score) and prepare it to be displayed """
		self.score_text = " x " + str(score)
		self.score_text_image = self.font.render(self.score_text, True, (255, 255, 255))
		self.score_text_rect = self.score_text_image.get_rect()
		self.score_text_rect.top = 5
		self.score_text_rect.left = self.pumpkin.get_tilesize()

	def refresh(self):
		""" Display the sprite and the text """
		self.pumpkin.draw()
		self.surface.blit(self.score_text_image, self.score_text_rect)

class LiveArea(pygame.sprite.Sprite):
	def __init__(self, surface, life=5):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface

		self.image = ImageLoader.get_single_sprite("SPRITE_GRAVE")
		self.rect = self.image.get_rect()
		self.rect.top = self.image.get_height()
		self.rect.left = self.image.get_width()
		self.group = pygame.sprite.GroupSingle(self)	
		
		self.font = pygame.font.Font(None, 36)
		self.update_text(life)

	def update_text(self, life):
		""" Update the text content (number of life) and prepare it to be displayed """
		self.life_text = " x " + str(life)
		if life == 1:
			self.life_text_image = self.font.render(self.life_text, True, (255, 0, 0))
		else:
			self.life_text_image = self.font.render(self.life_text, True, (255, 255, 255))
		self.life_text_rect = self.life_text_image.get_rect()
		self.life_text_rect.top = self.image.get_height() + 5
		self.life_text_rect.left = self.image.get_width() * 2 

	def refresh(self):
		""" Display the sprite and the text """
		self.group.draw(self.surface)
		self.surface.blit(self.life_text_image, self.life_text_rect)