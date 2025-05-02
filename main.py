import pygame
from constants import *
from player import Player
from circleshape import CircleShape, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import PLAYER_RADIUS




def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0  # initialize dt

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print("Screen width: 1280")
  print("Screen height: 720")

  # Create sprite groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  
  # Set containers class attributes
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)

  # Create player and field

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create player and add to groups
  
  field = AsteroidField()

  shot = pygame.sprite.Group()

  # Add player to relevant groups
  updatable.add(player)
  drawable.add(player)
  Shot.containers = (shot, updatable, drawable)
   


  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))  # fill the screen with black

    
    # Update and draw
    updatable.update(dt)

    for asteroid in asteroids:
       if player.collides_with(asteroid):
          print("Game over!")
          pygame.quit()
          exit()

    for asteroid in asteroids:
       for bullet in shot:
           if bullet.collides_with(asteroid):
              asteroid.split()
              bullet.kill()

    for asteroid in asteroids:
       if player.collides_with(asteroid):
          print("Game over!")
          pygame.quit()
          exit()

    # Draw everything
    for obj in drawable:
        obj.draw(screen)
    
 
    pygame.display.flip() 
    dt = clock.tick(60) / 1000

  pygame.quit()

if __name__ == "__main__":
   main()
