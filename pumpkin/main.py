#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from gameobjects import ground, player, pumpkin, scene, utils

class PumpkinObsession():
	def __init__(self):
		#Initialize pygame
		pygame.init()

		#Playing the celisoft intro video if not on Mac (movie module not implemented)
		if sys.platform != "darwin":
			lIntroScene = scene.MovieScene("MOVIE_CELISOFT_INTRO")
			lIntroScene.start()
			while lIntroScene.is_movie_playing():
				pygame.time.wait(60)
			lIntroScene.stop()
		else:
			print "Skip introduction video : not compatible with Darwin / MacOS"

		#Show the game splash screen during 1 second
		lInitScene = scene.TransitionScene("IMG_GAME_INIT")
		lInitScene.clear_screen()
		displayInitScene = True
		while displayInitScene:
			lInitScene.clear_screen()
			lInitScene.display()
			pygame.display.flip()
			pygame.time.wait(1000)
			displayInitScene = False

		#Create background music object & launching
		pygame.mixer.music.load(utils.SoundLoader.get_music("BG_MUSIC"))
		pygame.mixer.music.set_volume(0.25)
		pygame.mixer.music.play(-1)

		#Create game sounds object
		self.snd_get_pumpkin = pygame.mixer.Sound(utils.SoundLoader.get_sound("SND_GET_PUMPKIN"))
		self.snd_loose_game = pygame.mixer.Sound(utils.SoundLoader.get_sound("SND_LOOSE_GAME"))

		#Initalize the main game menu
		self.menu_scene = scene.MenuScene("IMG_GAME_INIT")
		self.menu_scene.add_menu_entry(scene.MenuSceneEntry("Play"))
		self.menu_scene.add_menu_entry(scene.MenuSceneEntry("Quit"))

		#Initialize the game scene with player and pumpkin manager
		self.game_scene = scene.GameScene()
		self.player = player.Player(self.game_scene)
		self.pumpkin_manager = pumpkin.PumpkinManager(self.game_scene.screen)
		self.ground = ground.Ground(self.game_scene.screen)

		#The game is not yet started, paused and not ended
		self.game_started = False
		self.game_ended = False
		self.game_paused = False

		#Allow key repeat
		pygame.key.set_repeat(50, 50)
		
		#Add a USEREVENT that will be used to generate a pumpkin every 2 seconds 
		pygame.time.set_timer(pygame.USEREVENT, 2000)

		#Add a USEREVENT that will reset notifaction area every 3.5 seconds 
		pygame.time.set_timer(pygame.USEREVENT+1, 3500)

		self.clock = pygame.time.Clock()

		#Cycle while the game is not finished
		while not self.game_ended:
			if self.game_started:	
				#Game loop
				self.game_scene.clear_screen()
				self.game_scene.refresh()

				if self.game_paused:
					self.game_scene.update_notification_area("Game paused")

					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							self.game_paused = False
				else:
					#Set the player waiting position
					self.player.wait()
					self.check_game_event()

					#Check if the user catch something
					if self.pumpkin_manager.collide_with_player(self.player):
						self.player.blink()
						self.snd_get_pumpkin.play()
						levelup = self.player.score_update()
						if levelup:
							#Increase the game speed
							self.pumpkin_manager.increase_pumpkin_speed(self.player.level)
					elif self.pumpkin_manager.collide_with_ground(self.ground):
						self.player.loose_live()
						if self.player.get_lives() == 0:
							self.reset()
							
							#Stop the game background music
							pygame.mixer.music.stop()

							#Play loose game sound
							self.snd_loose_game.play()
							
							#Display the loose game scene if the player loose the game
							self.end_scene = scene.TransitionScene("IMG_END")
							self.end_scene.clear_screen()
							self.end_scene.display()
							pygame.display.flip()
							pygame.time.wait(4500)

							#Restart the background music
							pygame.mixer.music.play(-1)

							#Back to start menu
							self.game_started = False
					
					#Display all pumpkins
					self.pumpkin_manager.move_and_draw()
				
				#Display the ground
				self.ground.draw()
			
				#Display the player
				self.player.draw()
			else:
				#Menu loop
				self.menu_scene.clear_screen()
				self.menu_scene.display()
				self.check_menu_event()

			#We only need 60 FPS not more (avoid screen blink)
			pygame.time.wait(60)
			self.clock.tick(60)
			pygame.display.flip()

		#Cleanly exit pygame
		pygame.quit()

	def check_menu_event(self):
		""" Check menu events and do something adapted to """
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					self.menu_scene.update_cursor_position()
				elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
					if self.menu_scene.get_selection() == 0:
						self.game_started = True
					else:
						self.game_ended = True
			elif event.type == pygame.QUIT:
				self.game_ended = True

	def check_game_event(self):
		""" Check game events and do something adapted to """
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT:
				#Create a new pumpkin
				self.pumpkin_manager.generate_pumpkin()					
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.player.move_right()
				elif event.key == pygame.K_LEFT:
					self.player.move_left()
				elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					self.player.jump()
				elif event.key == pygame.K_f:
					self.game_scene.toggle_fullscreen()
				elif event.key == pygame.K_ESCAPE or event.key == pygame.K_h:
					self.game_paused = True
				elif event.key == pygame.K_q:
					self.game_ended = True
			elif event.type == pygame.USEREVENT+1:
				#Erase the notification
				self.game_scene.reset_notification_area()
			elif event.type == pygame.QUIT:
				self.game_ended = True

	def reset(self):
		""" Reset game data to replay """
		#Reset player
		self.player.reset_data()
						
		#Reset game scene
		self.game_scene.reset()
							
		#Reset pumpkin manager
		self.pumpkin_manager.reset()

def start():
	print "Starting pumpkin obsession"
	PumpkinObsession()

if __name__ == "__main__":
	start()
