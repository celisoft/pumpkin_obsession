# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from utils import ImageLoader

class Scene():
	base_title = "Pumpkin obsession"
	scene_default_width = 1024
	scene_default_height = 768
	
	def __init__(self, width = None, height=None):
		if (width is None) | (height is None):
			self.screen = pygame.display.set_mode(( self.scene_default_width , self.scene_default_height ))
		else:
			self.screen = pygame.display.set_mode(( width , height ))
		pygame.display.set_caption(self.base_title)
		pygame.display.set_icon(ImageLoader.getSingleSprite("SPRITE_PUMPKIN_ICO"))
	
	def updateTitle(self, title):
		pygame.display.set_caption(self.base_title + " - " + title)

	def toggleFullScreen(self):
		pygame.display.toggle_fullscreen()

	def clearScreen(self):
		self.screen.fill((0, 0, 0))
		
class TransitionScene(Scene):
	def __init__(self, img_code):
		Scene.__init__(self)
		self.image = ImageLoader.getImage(img_code)
		self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))

	def display(self):
		self.screen.blit(self.image, self.image.get_rect())
		
class MenuScene(Scene):	
	def __init__(self, bg_code):
		Scene.__init__(self)

		self.menuentries = {}
		self.menu_size = 0

		self.background = ImageLoader.getImage(bg_code)
		self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

	def addMenuEntry(self, menuEntry):
		self.menuentries.update({self.menu_size: menuEntry})
		self.menu_size += 1

	def display(self):
		self.screen.blit(self.background, self.background.get_rect())
		pos_y = 0
		for menuentry_key, menuentry in self.menuentries.items():
			pos_y = self.screen.get_height()/3 + (menuentry_key * menuentry.getPixelStep())
			menuentry.display(self.screen, self.screen.get_width()/2, pos_y)

class MenuSceneEntry():
	font_type = None
	font_size = 40
	font_color = (255, 255, 255)
	
	def __init__(self, text, command = None):
		self.font = pygame.font.Font(self.font_type, self.font_size)
		self.text = self.font.render(text, True, self.font_color)

	def getPixelStep(self):
		return self.font_size + 5
		
	def display(self, screen, x, y):
		text_rect = self.text.get_rect(centerx=x, centery=y)
		screen.blit(self.text, text_rect)	

class GameScene(Scene):
	def __init__(self):
		Scene.__init__(self)

		