import pygame as pg
import pygame_gui as pgui
from .main_display import MainDisplay
from .resource_panel import ResourcePanel
from .panel import Panel
from game.events import new_game, load_game, economy_cycle

class Gui:

    def __init__(self, game, manager, window_surface):
        self.game = game
        self.manager = manager
        self.window_surface = window_surface
        self.width, self.height = window_surface.get_size()
        self.load_background()
        self.window = pgui.elements.UIPanel(manager = manager, starting_layer_height = 1, relative_rect = pg.Rect((0,0),(self.width, self.height)))
        self.window.set_image(pg.image.load('images/transparent.png'))
        w, h, x, y = self.width, self.height, 0, 0
        self.main_display = MainDisplay(self,size=(w,h),pos=(x,y))


    def update(self):
        pass


    def change_main_display(self):
        pass


    def load_background(self):
        background = pg.image.load('images/background.png').convert_alpha()
        self.window_surface.blit(background,(0,0))
