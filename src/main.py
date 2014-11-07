#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from gameobjects import player, pumpkin, scene

BG_MUSIC = "../data/sounds/music.ogg"

def run():
	pygame.init()

	lIntroScene = scene.MovieScene("MOVIE_CELISOFT_INTRO")
	lIntroScene.start()
	while lIntroScene.isPlayingMovie():
		pygame.time.wait(60)
	lIntroScene.stop()
		
	lInitScene = scene.TransitionScene("IMG_GAME_INIT")
	lInitScene.clearScreen()

	displayInitScene = True
	while displayInitScene:
		lInitScene.clearScreen()
		lInitScene.display()
		pygame.display.flip()
		pygame.time.wait(1000)
		displayInitScene = False

	pygame.mixer.music.load(BG_MUSIC)
	pygame.mixer.music.play()
		
	lMenuScene = scene.MenuScene("IMG_GAME_INIT")
	lMenuScene.addMenuEntry(scene.MenuSceneEntry("(J)OUER"))
	lMenuScene.addMenuEntry(scene.MenuSceneEntry("(Q)UITTER"))

	lGameScene = scene.GameScene()
	lPlayer = player.Player(lGameScene.screen)
	#lPumpkins = pygame.sprite.OrderedUpdates()
	#lPumpkins.add(pumpkin.Pumpkin(lGameScene.screen))

	gameStarted = False
	gameEnded = False
	
	while not gameEnded:
		if gameStarted:	
			lGameScene.clearScreen()
			lPlayer.wait()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						lPlayer.moveRight()
					elif event.key == pygame.K_LEFT:
						lPlayer.moveLeft()
					elif event.key == pygame.K_SPACE:
						lPlayer.jump()
					elif event.key == pygame.K_f:
						lGameScene.toggleFullScreen()
				elif event.type == QUIT:
					gameEnded = True
			lPlayer.draw()
			#lPumpkins.draw(lGameScene)
		else:
			lMenuScene.clearScreen()
			lMenuScene.display()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_j:
						gameStarted = True
					elif event.key == pygame.K_q:
						gameEnded = True
				elif event.type == QUIT:
					gameEnded = True

		pygame.time.wait(60)
		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	run()