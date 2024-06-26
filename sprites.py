import pygame
from settings import *
from random import randint, choice
from timer import Timer

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)


class Water(Generic):
    def __init__(self, pos, frames, groups,):
             
        # animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos = pos, 
            surf = self.frames[self.frame_index], 
            groups = groups,
            z = LAYERS['water'])
        
    def animate(self,dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self,dt):
        self.animate(dt)

class WildFlower(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)


class Tree(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)

        # tree attributes
        self.health = 5
        self.alive = True
        stump_path = f'graphics/stumps/{"small" if name == "Small" else "large"}.png'
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()
        self.invul_timer = Timer(200)

        # apples
        self.apple_surf = pygame.image.load('graphics/fruit/apple.png')
        self.apples_pos = APPLE_POS[name]
        self.apple_sprites = pygame.sprite.Group()
        self.create_fruit()

    def damage (self):
        # damaging the tree
        self.health -= 1 

        # remove an apple
        if len(self.apple_sprites.sprites()) > 0:
            random_apple = choice(self.apple_sprites.sprites())
            random_apple.kill()

    def create_fruit(self):
        for pos in self.apples_pos:
            if randint(0,10) > 3:
                x = pos [0] + self.rect.left 
                y = pos [1] + self.rect.top

                # contrain apples to screen width - not working
                x = max(0, min(x, SCREEN_WIDTH - TILE_SIZE))
                y = max(0, min(y, SCREEN_HEIGHT - TILE_SIZE))
                
                Generic(
                    pos = (x, y),
                    surf = self.apple_surf, 
                    groups = [self.apple_sprites,self.groups()[0]],
                    z = LAYERS ['fruit']
                )


                print(f"Apple created at {(x, y)} in layer {LAYERS['fruit']}")




