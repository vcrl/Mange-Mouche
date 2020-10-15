import pygame, random
from .settings import *

all_sprites = pygame.sprite.Group()
snake = pygame.sprite.Group()
body = pygame.sprite.Group()
food = pygame.sprite.Group()

class Label(pygame.sprite.Sprite):
    def __init__(self, color):
        self.groups = all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.font = pygame.font.SysFont("Ubuntu", 20)
        self.text = ""
        self.pos = (0, 0)
        self.color = color
    
    def update(self):
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites, snake
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.head = pygame.image.load(SNAKE)
        self.head = pygame.transform.smoothscale(self.head, (TILESIZE, TILESIZE))
        self.image = self.head
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 
        self.rect.y = HEIGHT / 2

        self.direction = "-"
        self.points = 0
        self.lose = False

        self.add_body_snd = pygame.mixer.Sound(ADD_BODY_SND)
        self.add_body_snd.set_volume(VOLUME)

    def add_body(self):
        new_body = Body(self.rect.x, self.rect.y)
    
    def update(self):
        cur_x = self.rect.x
        cur_y = self.rect.y

        if self.direction == "L":
            self.image = pygame.transform.rotate(self.head, -90)
            self.rect.x -= TILESIZE
        if self.direction == "R":
            self.image = pygame.transform.rotate(self.head, 90)
            self.rect.x += TILESIZE

        if self.direction == "U":
            self.image = pygame.transform.rotate(self.head, 180)
            self.rect.y -= TILESIZE
        if self.direction == "D":
            self.image = pygame.transform.rotate(self.head, 0)
            self.rect.y += TILESIZE

        if self.rect.x >= WIDTH:
            self.rect.x = 0 + 32
        if self.rect.x <= 0:
            self.rect.x = WIDTH
        
        if self.rect.y >= HEIGHT:
            self.rect.y = 0 + 32
        if self.rect.y <= 0:
            self.rect.y = HEIGHT

        for snake_body in body:
            x = snake_body.get_x()
            y = snake_body.get_y()
            snake_body.set_pos(cur_x, cur_y)
            cur_x = x
            cur_y = y

        collision_body = pygame.sprite.spritecollide(self, body, True)
        if collision_body:
            self.kill()
            self.lose = True
        
        collision_food = pygame.sprite.spritecollide(self, food, True)
        if collision_food:
            self.add_body()
            self.points += 1
            Food()
            print(self.points)
            self.add_body_snd.play()

class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites, food
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.current_sprite = 0
        self.image = pygame.image.load(FLY1)
        self.image = pygame.transform.smoothscale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(32, WIDTH - 32)
        self.rect.y = random.randint(32, HEIGHT - 32)
        self.sound = pygame.mixer.Sound(FLY_SND)
        self.sound.set_volume(VOLUME)
        self.sound.play()
    
    def update(self):
        self.animate(FLY_ANIM, 1.9)

    def animate(self, ANIMATION, speed):
        self.current_sprite += speed

        if self.current_sprite >= len(ANIMATION):
            self.current_sprite = 0

        self.image = pygame.image.load(ANIMATION[int(self.current_sprite)])
        self.image = pygame.transform.smoothscale(self.image, (TILESIZE, 25))

class Body(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, body
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(BODY)
        self.image = pygame.transform.smoothscale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y
    
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y