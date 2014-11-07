# -*- coding: utf-8 -*-

import os
from pygame import image

class ImageLoader():	
	images = {
		"IMG_GAME_BRAND":"../data/images/celisoft.png",
		"IMG_GAME_INIT":"../data/images/pumpkin.jpg"
	}
		
	sprites = {
		"SPRITE_PUMPKIN":"../data/sprites/pumpkin.png"
	}	

	spritesheets = {
		"SHEET_PLAYER":"../data/sprites/player_spritesheet.png",
	}

	@classmethod
	def getImage(self, code):
		for img_code, img_path in self.images.items():
			if img_code == code:
				if os.path.exists(img_path):
					return image.load(img_path)
				else:
					raise "ImageLoader cannot load image [" + img_path + "]."

	@classmethod
	def getSingleSprite(self, code):
		for sprite_code, sprite_path in self.sprites.items():
			if sprite_code == code:
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise "ImageLoader cannot load sprite [" + sprite_path + "]."

	@classmethod
	def loadSpritesheet(self, code):
		for sprite_code, sprite_path in self.spritesheets.items():
			if sprite_code == code:
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise "ImageLoader cannot load sprite [" + sprite_path + "]."

class SpriteSheet():	
	def __init__(self, code):
		self.sheet_image = ImageLoader.loadSpritesheet(code)
		
	def split(self):
		raise NotImplemented
		
class PlayerSpriteSheet(SpriteSheet):
	square_size = 128
	
	def __init__(self, code):
		SpriteSheet.__init__(self, code)

	def split(self):
		sprites = []
		for s in range(9):
			print self.square_size*s
			sprites.append(self.sheet_image.subsurface(self.square_size*s, 0, self.square_size, self.square_size))
		return sprites
		