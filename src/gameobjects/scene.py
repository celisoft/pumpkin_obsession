# -*- coding: utf-8 -*-

import pygame
from utils import ImageLoader, MovieLoader
import area

class Scene():
	base_title = "Pumpkin obsession"
	scene_default_width = 800
	scene_default_height = 600
	
	def __init__(self, width = None, height=None):
		if (width is None) | (height is None):
			self.screen = pygame.display.set_mode(( self.scene_default_width , self.scene_default_height ))
		else:
			self.screen = pygame.display.set_mode(( width , height ))
		pygame.display.set_caption(self.base_title)
		pygame.display.set_icon(ImageLoader.get_single_sprite("SPRITE_PUMPKIN_ICO"))
	
	def update_title(self, text):
		""" Update the window title by adding the text argument to the base title """
		pygame.display.set_caption(self.base_title + " - " + text)

	def toggle_fullscreen(self):
		""" Switch to fullscreen mode """
		pygame.display.toggle_fullscreen()

	def clear_screen(self):
		""" Erase everything from the screen and set a background color """
		self.screen.fill((0, 0, 0))
		
class TransitionScene(Scene):
	def __init__(self, img_code):
		Scene.__init__(self)
		self.image = ImageLoader.get_image(img_code)
		self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))

	def display(self):
		""" Display the image """
		self.screen.blit(self.image, self.image.get_rect())

class MovieScene(Scene):
	def __init__(self, video_code):
		Scene.__init__(self)
		self.movie = MovieLoader.get_movie("MOVIE_CELISOFT_INTRO")
		self.movie.set_display(self.screen, self.screen.get_rect())

	def start(self):
		""" Start playing the movie """
		self.movie.play()

	def is_movie_playing(self):
		""" Check if the movie is still playing (True) or not (False) """
		return self.movie.get_busy()

	def stop(self):
		""" Stop the movie and set to None the movie attribute in order to avoid segfault """
		self.movie.stop()
		self.movie = None
		
class MenuScene(Scene):	
	def __init__(self, bg_code):
		Scene.__init__(self)

		self.menuentries = {}
		self.menu_size = 0		
		self.background = ImageLoader.get_image(bg_code)
		self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

		self.cursor = ImageLoader.get_single_sprite("SPRITE_HAND")
		self.cursor_rect = self.cursor.get_rect()			

		self.left = self.screen.get_width()/8
		self.right = self.screen.get_width()/2.1
		self.cursor_rect.left = self.left
		self.cursor_rect.top = self.screen.get_height()*2/3 + self.cursor.get_height()/3
		self.selection = 0

	def add_menu_entry(self, menuEntry):
		""" Add a menu entry """
		self.menuentries.update({self.menu_size: menuEntry})
		self.menu_size += 1

	def update_cursor_position(self):
		""" Set the position oh the skeleton hand """
		if self.cursor_rect.left == self.left:
			self.cursor_rect.left = self.right
			self.selection = 1
		else:
			self.cursor_rect.left = self.left
			self.selection = 0

	def get_selection(self):
		return self.selection

	def display(self):
		""" Display the menu, that's to say all menu entries """
		self.screen.blit(self.background, self.background.get_rect())
		self.screen.blit(self.cursor, self.cursor_rect)
		for menuentry_key, menuentry in self.menuentries.items():
			pos_x = self.screen.get_width()*(menuentry_key+1)*0.35
			pos_y = self.screen.get_height()*2.5/3
			menuentry.display(self.screen, pos_x, pos_y)

class MenuSceneEntry():
	font_type = None
	font_size = 40
	font_color = (255, 255, 255)
	
	def __init__(self, text, command = None):
		self.font = pygame.font.Font(self.font_type, self.font_size)
		self.text = self.font.render(text, True, self.font_color)
		
	def display(self, screen, x, y):
		""" Display the menu entry """
		text_rect = self.text.get_rect(centerx=x, centery=y)

		encadre = pygame.Rect(text_rect.left -10, text_rect.top -5, text_rect.width + 25, text_rect.height + 10)
		
		pygame.draw.rect(screen, self.font_color, encadre, 1)
		screen.blit(self.text, text_rect)	

class GameScene(Scene):
	def __init__(self):
		Scene.__init__(self)

		self.background = ImageLoader.get_image("IMG_GAME_BG")
		self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))
		
		width = self.screen.get_width() / 6
		height = self.screen.get_height()
		self.info_zone = pygame.Surface((width, height))
		self.info_zone.fill((0, 0, 0))
		self.info_zone.set_colorkey((0,0,0))
		self.rect = self.info_zone.get_rect()
		self.rect.left = self.screen.get_width() - width

		self.score_area = area.ScoreArea(self.info_zone)
		self.life_area = area.LiveArea(self.info_zone)
		self.notif_area = area.NotificationArea(self.screen)

		self.update_score_area(0)
		self.update_life_area(5)
		self.update_notification_area("Catch a max of pumpkins !")

	def update_score_area(self, score):
		""" Update the score area """
		self.score_area.update_text(score)

	def update_life_area(self, life):
		""" Update the life area """
		self.life_area.update_text(life)

	def update_notification_area(self, txt):
		""" Update the notification area """
		self.notif_area.update_text(txt)

	def reset_notification_area(self):
		""" Used to reset the game notification area """
		self.notif_area.reset_text()
		
	def get_surface(self):
		""" Screen getter """
		return self.screen

	def refresh(self):
		""" Refresh the screen """
		self.info_zone.fill((0, 0, 0))
		
		self.score_area.refresh()
		self.life_area.refresh()
		
		self.screen.blit(self.background, self.background.get_rect())
		self.notif_area.refresh()
		self.screen.blit(self.info_zone, self.rect)
		