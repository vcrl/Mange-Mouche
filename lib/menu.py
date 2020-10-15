import pygame, sys, pygame_menu
from .sprites import Label, all_sprites
from .settings import *

class Menu:
    def __init__(self, engine):
        pygame.init()
        self.engine = engine
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mange-Mouche !")
        self.state = "running"
        self.clock = pygame.time.Clock()

        self.play_snd = pygame.mixer.Sound(PLAY_SND)
        self.play_snd.set_volume(VOLUME)
    
    def load_data(self):
        self.menu = pygame_menu.Menu(639, 639, 'Mange-Mouche', theme=pygame_menu.themes.THEME_GREEN)
        self.menu.add_button('Lancer une partie', self.start)
        self.menu.add_button('Quitter', pygame_menu.events.EXIT)
    
    def start(self):
        self.play_snd.play()
        self.engine.run()
        self.menu.kill()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def update(self):
        all_sprites.update()

    def draw(self):
        all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.load_data()
        while self.state == "running":
            self.events()
            self.update()
            self.draw()
            self.menu.mainloop(self.screen)
            self.clock.tick(7)