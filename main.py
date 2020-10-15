from lib.menu import Menu
from lib.engine import Engine

if __name__ == "__main__":
    engine = Engine()
    menu = Menu(engine)
    menu.run()