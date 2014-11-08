# -*- coding: utf-8 -*-

import os
from pygame import image, movie

class ImageLoader():	
	images = {
		"IMG_GAME_INIT":"../data/images/pumpkin_obsession.png"
	}
		
	sprites = {
		"SPRITE_PUMPKIN":"../data/sprites/pumpkin.png",
		"SPRITE_PUMPKIN_ICO":"../data/sprites/pumpkin_ico.png"
	}	

	spritesheets = {
		"SHEET_PLAYER":"../data/sprites/player_spritesheet.png"
	}

	@classmethod
	def get_image(self, code):
		""" Return the image associated to the given code """
		for img_code, img_path in self.images.items():
			if img_code == code:
				if os.path.exists(img_path):
					return image.load(img_path)
				else:
					raise Exception("ImageLoader cannot load image [" + img_path + "] -> File does not exist.")

	@classmethod
	def get_single_sprite(self, code):
		""" Return the sprite associated to the given code """
		for sprite_code, sprite_path in self.sprites.items():
			if sprite_code == code:
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise Exception("ImageLoader cannot load sprite [" + sprite_path + "] -> File does not exist.")

	@classmethod
	def load_spritesheet(self, code):
		""" Return the spritesheet associated to the given code """
		for sprite_code, sprite_path in self.spritesheets.items():
			if sprite_code == code:
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise Exception("ImageLoader cannot load spritesheet [" + sprite_path + "] -> File does not exist.")

class MovieLoader():
	movies = {
		"MOVIE_CELISOFT_INTRO":"../data/movies/celisoft.mpg"
	}

	@classmethod
	def get_movie(self, code):
		""" Return the movie associated to the given code """
		for movie_code, movie_path in self.movies.items():
			if movie_code == code:
				if os.path.exists(movie_path):
					return movie.Movie(movie_path)
				else:
					raise Exception("ImageLoader cannot load image [" + img_path + "] -> File does not exist.")
	
class SpriteSheet():	
	def __init__(self, code):
		self.sheet_image = ImageLoader.load_spritesheet(code)
		
	def split(self):
		raise NotImplemented
		
class PlayerSpriteSheet(SpriteSheet):
	square_size = 128
	
	def __init__(self, code):
		SpriteSheet.__init__(self, code)

	def split(self):
		""" Split into multiple sprites the player spritesheet """
		sprites = []
		for s in range(9):
			sprites.append(self.sheet_image.subsurface(self.square_size*s, 0, self.square_size, self.square_size))
		return sprites
		