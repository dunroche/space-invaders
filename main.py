import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from constants import PLAYER_RADIUS

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0  # initialize dt

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print("Screen width: 1280")
  print("Screen height: 720")

  # Create groups
  updatable = []
  drawable = []

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  updatable.append(player)
  drawable.append(player)

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))  # fill the screen with black

    # Update all updatables

    for obj in updatable:
      obj.update(dt)

    # Draw all drawables

    for obj in drawable:
      obj.draw(screen)
    
    #player.update(dt)
    #player.draw(screen)
    pygame.display.flip()   # update the full display

    dt = clock.tick(60) / 1000
  pygame.quit()

if __name__ == "__main__":
   main()
