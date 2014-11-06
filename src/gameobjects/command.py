# -*- coding: utf-8 -*-

import os, sys
import pygame

class Command():
	@classmethod
	def execute(self):
		raise NotImplemented

class ExitCommand(Command):	
	@classmethod
	def execute (self):
		print "Exit required by user [" + os.getlogin() + "]"
		pygame.quit()	

