import pygame as pg
import pygame_gui as pgui
from .panels import *


class Gui:

    def __init__(self, game, manager, window_surface):
        self.game = game
        self.manager = manager
        self.window_surface = window_surface
        self.width, self.height = window_surface.get_size()
        self.load_background()
        self.window = pgui.elements.UIPanel(manager = manager, starting_layer_height = 1, relative_rect = pg.Rect((0,0),(self.width, self.height)))
        self.window.set_image(pg.image.load('images/transparent.png'))

        self.toolbar = Toolbar(self)
        self.action_menu = ActionMenu(self)
        self.notification_display = NotificationDisplay(self)
        self.viewport = Viewport(self)
        self.submenu = SubMenu(self)
        self.alert_window = AlertWindow(self, self.viewport)


    def gui_sub_panel(self,pos,size,container=None):
        if container is None:
            container = self.window

        return pgui.elements.UIPanel(
            relative_rect=pg.Rect(pos,size),
            container=container,
            manager=self.manager,
            starting_layer_height=1
        )


    def update(self):
        pass


    def load_background(self):
        background = pg.image.load('images/background.png').convert_alpha()
        self.window_surface.blit(background,(0,0))
