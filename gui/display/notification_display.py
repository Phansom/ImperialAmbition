from gui.panel import Panel
import pygame_gui as pgui
import pygame as pg



class NotificationDisplay:
    def __init__(self, gui, container):
        self.gui = gui
        self.main_display = container
        size, pos = (container.size[0] * 0.1, container.size[1] * 0.85), (container.size[0] * 0.9, container.size[1] * 0.05)
        self.pos = pos
        self.size = size
        self.display_panel = Panel(gui, gui, self.pos, self.size)
        self.window = self.display_panel.window


    def print(self, text):
        pass

