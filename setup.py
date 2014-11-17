#!/usr/bin/env python

from distutils.core import setup

data_files=['data/images/*.png', 'data/movies/*.mpg', 'data/sounds/*', 'data/sprites/*']

setup(
	name='Pumpkin_Obsession',
	version='0.1',
	license='BSD',
	description='Python arcade game with a skeleton and some pumpkins',
	author='Celine Liberal, Zoe Belleton',
	author_email='celine.liberal@mail.com',
	url='http://www.celisoft.com/games/pumpkin_obsession/',
	packages=['pumpkin', 'pumpkin.gameobjects'],
	package_data={'pumpkin': data_files },
	scripts=['pumpkin_obsession']
)
