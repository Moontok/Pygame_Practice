import pygame
from pygame.math import Vector2

from scripts.timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, semi_collision_sprites):
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
        self.semi_collision_sprites = semi_collision_sprites
        self.on_surface = {'floor': False, 'left': False, 'right': False}
        self.platform = None

        # Timers
        self.timers = {
            'wall jump': Timer(400),
            'wall slide block': Timer(250),
        }

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = Vector2(0, 0)

        if not self.timers['wall jump'].active:
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
        if (
            not self.on_surface['floor']
            and any((self.on_surface['left'], self.on_surface['right']))
            and not self.timers['wall slide block'].active
        ):
            self.direction.y = 0
            self.rect.y += self.gravity / 10 * dt
        else:
            self.direction.y += self.gravity / 2 * dt
            self.rect.y += self.direction.y * dt
            self.direction.y += self.gravity / 2 * dt

        if self.jump:
            if self.on_surface['floor']:
                self.direction.y = -self.jump_force
                self.timers['wall slide block'].activate()
                self.rect.bottom -= 1
            elif (
                any((self.on_surface['left'], self.on_surface['right']))
                and not self.timers['wall slide block'].active
            ):
                self.timers['wall jump'].activate()
                self.direction.y = -self.jump_force
                self.direction.x = 1 if self.on_surface['left'] else -1
            self.jump = False

        self.collision('vertical')
        self.semi_collision()

    def platform_move(self, dt):
        if self.platform:
            self.rect.topleft += self.platform.direction * self.platform.speed * dt       
    
    def check_contact(self):
        floor_rect = pygame.Rect(self.rect.bottomleft, (self.rect.width, 2))
        right_rect = pygame.Rect(
            self.rect.topright + Vector2(0, self.rect.height / 4), (2, self.rect.height / 2)
        )
        left_rect = pygame.Rect(
            self.rect.topleft + Vector2(-2, self.rect.height / 4), (2, self.rect.height / 2)
        )        
        collide_rects = [sprite.rect for sprite in self.collision_sprites]
        semi_collide_rects = [sprite.rect for sprite in self.semi_collision_sprites]

        # Collisions
        self.on_surface['floor'] = (
            True
            if floor_rect.collidelist(collide_rects) >= 0
            or floor_rect.collidelist(semi_collide_rects) >= 0
            and self.direction.y >= 0
            else False
        )
        self.on_surface['right'] = True if right_rect.collidelist(collide_rects) >= 0 else False
        self.on_surface['left'] = True if left_rect.collidelist(collide_rects) >= 0 else False

        self.platform = None
        sprites = self.collision_sprites.sprites() + self.semi_collision_sprites.sprites()
        for sprite in [sprite for sprite in sprites if hasattr(sprite, 'moving')]:
            if sprite.rect.colliderect(floor_rect):
                self.platform = sprite

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    if self.rect.left <= sprite.rect.right and int(self.old_rect.left) >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.left and int(self.old_rect.right) <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else: # Vertical
                    if self.rect.top <= sprite.rect.bottom and int(self.old_rect.top) >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        if hasattr(sprite, 'moving'):
                            self.rect.top += 6
                    if self.rect.bottom >= sprite.rect.top and int(self.old_rect.bottom) <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    self.direction.y = 0

    def semi_collision(self):
        for sprite in self.semi_collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.rect.bottom >= sprite.rect.top and int(self.old_rect.bottom) <= sprite.old_rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.update_timers()
        self.input()
        self.move(dt)
        self.platform_move(dt)
        self.check_contact()