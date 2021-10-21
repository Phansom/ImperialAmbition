import pygame as pg
import pygame_gui as pgui
from .panel import Panel
from settings import DATA_BUTTON_NAMES, TOOLBAR_ELEMENTS

class MainDisplay:
    def __init__(self, gui, pos, size):
        self.gui = gui
        self.size = size
        self.pos = pos
        self.manager = gui.manager

        size, pos = (self.size[0] * 0.8, self.size[1] * 0.8), (self.size[0] * 0.1, self.size[1] * 0.05)
        self.main_panel = Panel(gui, gui, pos, size)

        size, pos = (self.size[0], self.size[1] * 0.05), (0, 0)
        self.toolbar = Panel(gui, gui, pos, size)

        size, pos = (self.size[0], self.size[1] * 0.15), (0,self.size[1] * 0.85)
        self.action_panel = Panel(gui, gui, pos, size)

        size, pos = (self.size[0] * 0.1, self.size[1] * 0.8), (0,self.size[1]*0.05)
        self.info_panel = Panel(gui, gui, pos, size)

        size, pos = (self.size[0] * 0.1, self.size[1] * 0.8), (self.size[0] * 0.9, self.size[1] * 0.05)
        self.notification_panel = Panel(gui, gui, pos, size)

        self.toolbar_elements = self.setup_toolbar_elements()

    def setup_toolbar_elements(self):
        buttons = {}
        size = self.toolbar.size
        x,y,w,h = 3, 3,size[1] - 9,size[1] - 11
        for i in range(len(TOOLBAR_ELEMENTS)):
            x_spacing = (w + x) * i
            item = TOOLBAR_ELEMENTS[i]
            pos = x + x_spacing, y
            size = w, h
            button = pgui.elements.UIButton(
                manager= self.manager,
                container = self.toolbar.panel,
                relative_rect = pg.Rect(pos, size),
                text = item
            )
            buttons[item] = button
        return buttons

    def update(self):
        pass



