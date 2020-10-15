import os

dir = os.path.dirname(__file__)

TILESIZE = 32
WIDTH = 64 * 10
HEIGHT = 64 * 10
FPS = 7

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game settings
VOLUME = 1.0

# Textures
SNAKE = os.path.join(dir, "../data/img/TETE.png")
BODY = os.path.join(dir, "../data/img/CORPS.png")
FOOD = os.path.join(dir, "../data/img/NOURRITURE.png")

FLY1 = os.path.join(dir, "../data/img/flyFly1.png")
FLYDEAD = os.path.join(dir, "../data/img/flyDead.png")
FLY_ANIM = [
    os.path.join(dir, "../data/img/flyFly1.png"),
    os.path.join(dir, "../data/img/flyFly2.png")
]

BG = os.path.join(dir, "../data/img/BACKGROUND.png")
GROUND = os.path.join(dir, "../data/img/GROUND.jpg")
PYGAME_POWERED = os.path.join(dir, "../data/img/icon.png")
BUTTON = os.path.join(dir, "../data/img/overlay_top.png")

# Sounds
ADD_BODY_SND = os.path.join(dir, "../data/sounds/add_body.ogg")
PLAY_SND = os.path.join(dir, "../data/sounds/play.ogg")
FLY_SND = os.path.join(dir, "../data/sounds/lose.ogg")