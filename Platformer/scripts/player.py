import pygame
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')

        # Rects
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        # Movement
        self.direction = Vector2(0, 0)
        self.speed = 200
        self.gravity = 1300

        # Collision
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    def move(self, dt):
        # Horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        # Vertical
        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt

        self.collision('vertical')


    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.rect.left:
                        self.rect.right = sprite.rect.left
                else: # Vertical
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)