#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import random

import pygame
from pygame.locals import *

from gameobjects import command, player, scene

BG_MUSIC = "../data/sounds/music.ogg"

def run():
	pygame.init()

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

	gameStarted = False
	gameEnded = False
	
	while not gameEnded:
		if gameStarted:
			lGameScene.clearScreen()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						lPlayer.moveRight()
					elif event.key == pygame.K_LEFT:
						lPlayer.moveLeft()
				elif event.type == QUIT:
					gameEnded = True
			lPlayer.draw()
			pygame.display.flip()
			lGameScene.clearScreen()
			lPlayer.stay()
			lPlayer.draw()
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
	command.ExitCommand().execute()

if __name__ == "__main__":
	run()