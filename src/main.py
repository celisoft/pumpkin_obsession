#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from gameobjects import player, pumpkin, scene

BG_MUSIC = "../data/sounds/music.ogg"

def run():
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

	#Launch the background music
	pygame.mixer.music.load(BG_MUSIC)
	pygame.mixer.music.play()

	#Initalize the main game menu
	lMenuScene = scene.MenuScene("IMG_GAME_INIT")
	lMenuScene.add_menu_entry(scene.MenuSceneEntry("(J)OUER"))
	lMenuScene.add_menu_entry(scene.MenuSceneEntry("(Q)UITTER"))

	#Initialize the game scene with player and pumpkin manager
	lGameScene = scene.GameScene()
	lPlayer = player.Player(lGameScene.screen)
	lPumpkins = pumpkin.PumpkinManager(lGameScene.screen)

	#The game is not yet started and is not ended
	gameStarted = False
	gameEnded = False

	#Add a USEREVENT that will be used to generate a pumpkin every 2 seconds 
	pygame.time.set_timer(pygame.USEREVENT, 2000)

	#Cycle while the game is not finished
	while not gameEnded:
		if gameStarted:	
			#Game loop
			lGameScene.clear_screen()

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
					elif event.key == pygame.K_SPACE:
						lPlayer.jump()
					elif event.key == pygame.K_f:
						lGameScene.toggle_fullscreen()
				elif event.type == QUIT:
					gameEnded = True

			#Check if the user catch something
			lPumpkins.collide_with_player(lPlayer)
					
			#Display the player sprite
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
				elif event.type == QUIT:
					gameEnded = True

		#We only need 60 FPS not more (avoid screen blink)
		pygame.time.wait(60)
		pygame.display.flip()

	#Cleanly exit pygame
	pygame.quit()

if __name__ == "__main__":
	run()