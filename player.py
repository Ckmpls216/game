import pygame
from config import *

class Bullet:
    def __init__(self, x, y, speed=10, color=YELLOW):
        self.rect = pygame.Rect(x, y, 20, 10)  # Larger size for better visibility
        self.speed = speed
        self.color = color

    def update(self):
        self.rect.x += self.speed
        print(f"Bullet at ({self.rect.x}, {self.rect.y}) moving to right")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player:
    def __init__(self, x, y, width, height, color=RED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = PLAYER_SPEED
        self.health = 100
        self.vel_y = 0
        self.on_ground = True
        self.bullets = []

        self.rect = pygame.Rect(x, y, width, height)

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed

    def jump(self):
        if self.on_ground:
            self.vel_y = -10
            self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.rect.y += self.vel_y
            self.vel_y += 1
            if self.rect.y >= PLAYER_Y:
                self.rect.y = PLAYER_Y
                self.on_ground = True
                self.vel_y = 0

    def fire_bullet(self):
        new_bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(new_bullet)
        print(f"Firing bullet. Total bullets: {len(self.bullets)}")

    def update_bullets(self, screen):
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.x > WIN_WIDTH:
                self.bullets.remove(bullet)
                print("Bullet removed")
            else:
                bullet.draw(screen)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print("Game Over")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
