import sys

import pygame

def run_game():
	#initialize the game and create a screen object
	pygame.init()
	screen = pygame.display.setmode((2560,1600))
	pygame.display.set_caption("Alien invasion")

	#Start the main loop of the game

	while True:
		#Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()



	#Make the most recently drawn screen visible.
	pygame.display.flip()

run_game()

