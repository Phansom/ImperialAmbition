import pygame as pg
import pygame_gui as pgui
from gui.panel import Panel
from settings import DATA_BUTTON_NAMES, TOOLBAR_ELEMENTS, ACTION_PANEL_ELEMENTS
from gui.display.notification_display import NotificationDisplay

class MainDisplay:
    def __init__(self, gui, pos, size):
        self.gui = gui
        self.size = size
        self.pos = pos
        self.manager = gui.manager
        self.window = gui.window

        size, pos = (self.size[0] * 0.8, self.size[1] * 0.85), (self.size[0] * 0.1, self.size[1] * 0.05)
        self.main_panel = Panel(gui, gui, pos, size)

        size, pos = (self.size[0], self.size[1] * 0.05), (0, 0)
        self.toolbar = Panel(gui, gui, pos, size)

        size, pos = (self.size[0], self.size[1] * 0.1), (0,self.size[1] * 0.9)
        self.action_panel = Panel(gui, gui, pos, size)

        size, pos = (self.size[0] * 0.1, self.size[1] * 0.85), (0,self.size[1]*0.05)
        self.info_panel = Panel(gui, gui, pos, size)

        self.notification_display = NotificationDisplay(gui, self)


        self.toolbar_elements = self.setup_toolbar_elements()
        self.action_panel_elements = self.setup_action_panel_elements()

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
                container = self.toolbar.window,
                relative_rect = pg.Rect(pos, size),
                text = item
            )
            buttons[item] = button
        return buttons

    def setup_action_panel_elements(self):
        buttons = {}
        size = self.action_panel.size
        x,y,w,h = size[0] * 0.01, size[1] * 0.1, size[0] * 0.1, size[1] * 0.7
        for i in range(len(ACTION_PANEL_ELEMENTS)):
            x_spacing = (w + x) * i
            item = ACTION_PANEL_ELEMENTS[i]
            pos = x + x_spacing, y
            size = w, h
            button = pgui.elements.UIButton(
                manager= self.manager,
                container = self.action_panel.window,
                relative_rect = pg.Rect(pos, size),
                text = item
            )
            buttons[item] = button
        return buttons


    def update(self):
        pass



