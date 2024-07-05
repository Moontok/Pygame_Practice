import pygame

import scripts.sprites as sprites
import scripts.settings as settings
import scripts.player as player
import scripts.groups as groups


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        # Groups
        self.all_sprites = groups.AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.semi_collision_sprites = pygame.sprite.Group()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        # tiles
        for layer in ['BG', 'Terrain', 'FG', 'Platforms']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                groups = [self.all_sprites]
                if layer == 'Terrain': groups.append(self.collision_sprites)
                if layer == 'Platforms': groups.append(self.semi_collision_sprites)
                match layer:
                    case 'BG': z = settings.Z_LAYERS['bg tiles']
                    case 'FG': z = settings.Z_LAYERS['fg']
                    case _: z = settings.Z_LAYERS['main']
                sprites.Sprite((x * settings.TILE_SIZE, y * settings.TILE_SIZE), surf, groups, z)

        # objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                self.player = player.Player(
                    (obj.x, obj.y),
                    self.all_sprites,
                    self.collision_sprites,
                    self.semi_collision_sprites,
                )

        # moving objects
        for obj in tmx_map.get_layer_by_name('Moving Objects'):
            if obj.name == 'helicopter':
                if obj.width > obj.height: # horizontal
                   mov_dir = 'x'
                   start_pos = (obj.x, obj.y + obj.height / 2)
                   end_pos = (obj.x + obj.width, obj.y + obj.height / 2)
                else: # vertical
                    mov_dir = 'y'
                    start_pos = (obj.x + obj.width / 2, obj.y)
                    end_pos = (obj.x + obj.width / 2, obj.y + obj.height)
                speed = obj.properties['speed']
                sprites.MovingSprite(
                    (self.all_sprites, self.semi_collision_sprites),
                    start_pos,
                    end_pos,
                    mov_dir,
                    speed,
                )


    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.player.hitbox_rect.center)