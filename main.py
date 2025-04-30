import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0  # initialize dt

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print("Screen width: 1280")
  print("Screen height: 720")

  # Create groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create player and add to groups
  
  updatable.append(player)
  drawable.append(player)

  field = AsteroidField()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))  # fill the screen with black

    # Update all objects

    for obj in updatable:
        obj.update(dt)

    # Draw all drawables

    for obj in drawable:
        obj.draw(screen)
    
 
    pygame.display.flip()   # update the full display

    dt = clock.tick(60) / 1000
  pygame.quit()

if __name__ == "__main__":
   main()
