import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print("Screen width: 1280")
  print("Screen height: 720")

  while True:
      screen.fill((0, 0, 0))  # fill the screen with black
      pygame.display.flip()   # update the full display
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
if __name__ == "__main__":
   main()
