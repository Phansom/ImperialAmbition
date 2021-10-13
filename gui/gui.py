import pygame as pg
import pygame_gui as pgui
from .main_display import MainDisplay

class Gui:

    def __init__(self, game, manager, window_surface, clock):
        self.game = game
        self.window_surface = window_surface
        self.clock = clock
        self.width, self.height = self.window_surface.get_size()
        self.manager = manager
        self.window = pgui.elements.UIPanel(
            relative_rect = pg.Rect((0,0), (self.width, self.height)),
            manager= self.manager,
            starting_layer_height = 0
        )

        loc = [0,0]
        size = [self.width, self.height]
        self.main_panel = MainDisplay(self, loc, size)


    def handle_button(self, button):
        if button in self.main_panel.data_buttons:
            self.main_panel.change_main_display(button.text)




