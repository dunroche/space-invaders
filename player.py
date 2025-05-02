import pygame
from circleshape import CircleShape, Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN



class Player(CircleShape):
	def __init__(self, x, y):
		self.shoot_timer = 0 # Timer in seconds
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0



	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if self.shoot_timer > 0:
			self.shoot_timer -= dt

		if keys[pygame.K_a]:
			self.rotate(-dt) # rotate left


		if keys[pygame.K_d]:
			self.rotate(dt) # rotate right
			

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)

		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt


	def shoot(self):
		direction = pygame.Vector2(0, -1).rotate(-self.rotation) # assuming up is 0 degrees
		velocity = direction * PLAYER_SHOOT_SPEED
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		Shot(self.position.x, self.position.y, velocity)

	

