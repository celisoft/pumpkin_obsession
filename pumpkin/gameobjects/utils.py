# -*- coding: utf-8 -*-

import os
from pygame import image, movie

class ImageLoader():	
	images = {
		"IMG_GAME_INIT":"../data/images/pumpkin_obsession.png",
		"IMG_GAME_BG":"../data/images/game_background.png",
		"IMG_END":"../data/images/end.png"
	}
		
	sprites = {
		"SPRITE_PUMPKIN":"../data/sprites/pumpkin.png",
		"SPRITE_PUMPKIN_ICO":"../data/sprites/pumpkin_ico.png",
		"SPRITE_GROUND":"../data/sprites/cubesol.png",
		"SPRITE_GRAVE":"../data/sprites/rip.png",
		"SPRITE_HAND":"../data/sprites/hand.png"
	}	

	spritesheets = {
		"SHEET_PLAYER":"../data/sprites/player_spritesheet.png"
	}

	@classmethod
	def update_path(self, path):
		""" Update path to local """
		root = __file__
		if os.path.islink(root):
			root = os.path.realpath(root)
		root = os.path.dirname(os.path.abspath(root))
		return root + "/" + path

	@classmethod
	def get_image(self, code):
		""" Return the image associated to the given code """
		for img_code, img_path in self.images.items():
			if img_code == code:
				img_path = self.update_path(img_path)
				if os.path.exists(img_path):
					return image.load(img_path)
				else:
					raise Exception("ImageLoader cannot load image [" + img_path + "] -> File does not exist.")

	@classmethod
	def get_single_sprite(self, code):
		""" Return the sprite associated to the given code """
		for sprite_code, sprite_path in self.sprites.items():
			if sprite_code == code:
				sprite_path = self.update_path(sprite_path)
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise Exception("ImageLoader cannot load sprite [" + sprite_path + "] -> File does not exist.")

	@classmethod
	def load_spritesheet(self, code):
		""" Return the spritesheet associated to the given code """
		for sprite_code, sprite_path in self.spritesheets.items():
			if sprite_code == code:
				sprite_path = self.update_path(sprite_path)
				if os.path.exists(sprite_path):
					return image.load(sprite_path)
				else:
					raise Exception("ImageLoader cannot load spritesheet [" + sprite_path + "] -> File does not exist.")

class MovieLoader():
	movies = {
		"MOVIE_CELISOFT_INTRO":"../data/movies/celisoft.mpg"
	}

	@classmethod
	def update_path(self, path):
		""" Update path to local """
		root = __file__
		if os.path.islink(root):
			root = os.path.realpath(root)
		root = os.path.dirname(os.path.abspath(root))
		return root + "/" + path

	@classmethod
	def get_movie(self, code):
		""" Return the movie associated to the given code """
		for movie_code, movie_path in self.movies.items():
			if movie_code == code:
				movie_path = self.update_path(movie_path)
				if os.path.exists(movie_path):
					return movie.Movie(movie_path)
				else:
					raise Exception("MovieLoader cannot load movie [" + movie_path + "] -> File does not exist.")

class SoundLoader():
	sounds = {
		"SND_GET_PUMPKIN":"../data/sounds/get_pumpkin.wav",
		"SND_LOOSE_GAME":"../data/sounds/end.wav"
	}

	musics = {
		"BG_MUSIC" : "../data/sounds/music.ogg"
	}

	@classmethod
	def update_path(self, path):
		""" Update path to local """
		root = __file__
		if os.path.islink(root):
			root = os.path.realpath(root)
		root = os.path.dirname(os.path.abspath(root))
		return root + "/" + path

	@classmethod
	def get_sound(self, code):
		""" Return the sound associated to the given code """
		for sound_code, sound_path in self.sounds.items():
			if sound_code == code:
				sound_path = self.update_path(sound_path)
				if os.path.exists(sound_path):
					return sound_path
				else:
					raise Exception("SoundLoader cannot load sound [" + sound_path + "] -> File does not exist.")

	@classmethod
	def get_music(self, code):
		""" Return the music associated to the given code """
		for music_code, music_path in self.musics.items():
			if music_code == code:
				music_path = self.update_path(music_path)
				if os.path.exists(music_path):
					return music_path
				else:
					raise Exception("SoundLoader cannot load music [" + music_path + "] -> File does not exist.")
				
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
		for s in range(10):
			sprites.append(self.sheet_image.subsurface(self.square_size*s, 0, self.square_size, self.square_size))
		return sprites
		
