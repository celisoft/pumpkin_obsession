#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from gameobjects import ground, player, pumpkin, scene

class PumpkinObsession():
	BG_MUSIC = "../data/sounds/music.ogg"
	SND_GET_PUMPKIN = "../data/sounds/get_pumpkin.wav"
	SND_LOOSE_GAME = "../data/sounds/end.wav"
	
	def __init__(self):
		#Initialize pygame
		pygame.init()

		#Playing the celisoft intro video
		lIntroScene = scene.MovieScene("MOVIE_CELISOFT_INTRO")
		lIntroScene.start()
		while lIntroScene.is_movie_playing():
			pygame.time.wait(60)
		lIntroScene.stop()

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
		pygame.mixer.music.load(self.BG_MUSIC)
		pygame.mixer.music.set_volume(0.25)
		pygame.mixer.music.play(-1)

		#Create game sounds object
		get_pumpkin_sound = pygame.mixer.Sound(self.SND_GET_PUMPKIN)
		loose_game_sound = pygame.mixer.Sound(self.SND_LOOSE_GAME)

		#Initalize the main game menu
		lMenuScene = scene.MenuScene("IMG_GAME_INIT")
		lMenuScene.add_menu_entry(scene.MenuSceneEntry("(J)OUER"))
		lMenuScene.add_menu_entry(scene.MenuSceneEntry("(Q)UITTER"))

		#Allow key repeat
		pygame.key.set_repeat(50, 50)

		#Initialize the game scene with player and pumpkin manager
		lGameScene = scene.GameScene()
		lPlayer = player.Player(lGameScene)
		lPumpkins = pumpkin.PumpkinManager(lGameScene.screen)
		lGround = ground.Ground(lGameScene.screen)

		#The game is not yet started and is not ended
		gameStarted = False
		gameEnded = False
	
		#Add a USEREVENT that will be used to generate a pumpkin every 2 seconds 
		pygame.time.set_timer(pygame.USEREVENT, 2000)

		lClock = pygame.time.Clock()

		#Cycle while the game is not finished
		while not gameEnded:
			if gameStarted:	
				#Game loop				
				lGameScene.clear_screen()
				lGameScene.refresh()
			
				#Set the player waiting position
				lPlayer.wait()
			
				for event in pygame.event.get():
					if event.type == pygame.USEREVENT:
						#Create a new pumpkin
						lPumpkins.generate_pumpkin()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RIGHT:
							lPlayer.move_right()
						elif event.key == pygame.K_LEFT:
							lPlayer.move_left()
						elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
							lPlayer.jump()
						elif event.key == pygame.K_f:
							lGameScene.toggle_fullscreen()
					elif event.type == pygame.QUIT:
						gameEnded = True

				#Check if the user catch something
				if lPumpkins.collide_with_player(lPlayer):
					get_pumpkin_sound.play()
					lPlayer.score_update()
				elif lPumpkins.collide_with_ground(lGround):
					lPlayer.loose_live()
					if lPlayer.get_lives() == 0:
						#Stop the game background music
						pygame.mixer.music.stop()

						#Play loose game sound
						loose_game_sound.play()
						
						#Display the loose game scene if the player loose the game
						lEndScene = scene.TransitionScene("IMG_END")
						lEndScene.clear_screen()
						lEndScene.display()
						pygame.display.flip()
						pygame.time.wait(4500)

						#Back to start menu
						gameStarted = False

				#Display the ground
				lGround.draw()
			
				#Display the player
				lPlayer.draw()

				#Display all pumpkins
				lPumpkins.move_and_draw()
			else:
				#Menu loop
				lMenuScene.clear_screen()
				lMenuScene.display()

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_j:
							gameStarted = True
						elif event.key == pygame.K_q:
							gameEnded = True
					elif event.type == pygame.QUIT:
						gameEnded = True

			#We only need 60 FPS not more (avoid screen blink)
			pygame.time.wait(60)
			lClock.tick(60)
			pygame.display.flip()

		#Cleanly exit pygame
		pygame.quit()

if __name__ == "__main__":
	PumpkinObsession()