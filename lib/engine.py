import pygame, sys
from .sprites import all_sprites, Snake, Food, Label
from .menu import Menu
from .settings import *

class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Classic Snake")
        self.state = "running"
        self.clock = pygame.time.Clock()
    
    def load_data(self):
        self.bg = pygame.image.load(GROUND)
        self.bg = pygame.transform.smoothscale(self.bg, (WIDTH, HEIGHT))
        self.snake = Snake()
        self.food = Food()

        self.overlay = pygame.image.load(BUTTON)

        self.fly_points = pygame.image.load(FLYDEAD)
        self.fly_points = pygame.transform.smoothscale(self.fly_points, (TILESIZE, 25))

        self.display_points = Label(WHITE)
        self.display_points.pos = (50, 22.5)

        self.intro = pygame.image.load(PYGAME_POWERED).convert_alpha()
        self.intro = pygame.transform.smoothscale(self.intro, (190, 75))

    def clear_game(self):
        self.snake.kill()
        self.food.kill()
        self.display_points.kill()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if self.snake.lose == True:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and self.snake.direction != "R":
                    self.snake.direction = "L"
                if event.key == pygame.K_d and self.snake.direction != "L":
                    self.snake.direction = "R"
                if event.key == pygame.K_z and self.snake.direction != "D":
                    self.snake.direction = "U"
                if event.key == pygame.K_s and self.snake.direction != "U":
                    self.snake.direction = "D"
                if event.key == pygame.K_h:
                    self.running = False
    
    def update(self):
        all_sprites.update()
        self.display_points.text = "{}".format(self.snake.points)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        #self.screen.blit(self.overlay, (WIDTH/2 - 95, 10))
        self.screen.blit(self.fly_points, (10, 10))
        self.screen.blit(self.intro, (WIDTH/2 - 90, 1))
        all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.load_data()
        while self.state == "running":
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            