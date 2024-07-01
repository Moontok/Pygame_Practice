import sys
from os.path import join

import pygame
from pytmx.util_pygame import load_pygame

import scripts.settings as settings
import scripts.level as level


class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
		pygame.display.set_caption('Pygame Platformer')
		self.clock = pygame.time.Clock()

		self.tmx_maps = {
			0: load_pygame(join('data', 'levels', 'omni.tmx')),
		}

		self.current_stage = level.Level(self.tmx_maps[0])


	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.current_stage.run(dt)
			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()