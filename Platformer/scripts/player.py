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
        self.jump = False
        self.jump_force = 900

        # Collision
        self.collision_sprites = collision_sprites
        self.on_surface = {'floor': False, 'left': False, 'right': False}

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

        if keys[pygame.K_SPACE]:
            self.jump = True

    def move(self, dt):
        # Horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        # Vertical
        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt
        self.collision('vertical')

        if self.jump:
            if self.on_surface['floor']:
                self.direction.y = -self.jump_force
            self.jump = False
        
    
    def check_contect(self):
        floor_rect = pygame.Rect(self.rect.bottomleft, (self.rect.width, 2))
        right_rect = pygame.Rect(self.rect.topright, (2, self.rect.height - 2))
        left_rect = pygame.Rect(self.rect.topleft, (2, self.rect.height - 2))
        
        collide_rects = [sprite.rect for sprite in self.collision_sprites]

        # Collisions
        self.on_surface['floor'] = True if floor_rect.collidelist(collide_rects) >= 0 else False

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else: # Vertical
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    self.direction.y = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        self.check_contect()