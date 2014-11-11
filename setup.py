#!/usr/bin/env python

from distutils.core import setup

setup(
	name='Pumpkin Obsession',
	version='1.0',
	license='BSD',
	description='Python arcade game with a skeleton and some pumpkins',
	author='Celine Liberal, Zoe Belleton',
	author_email='celine.liberal@mail.com',
	url='http://www.celisoft.com/games/pumpkin_obsession/',
	packages=['src', 'src.gameobjects'],
	include_package_data=True
)