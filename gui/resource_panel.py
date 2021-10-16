import pygame_gui
import pygame as pg
from gui.panel import Panel
from game.economy.resources import *

class ResourcePanel:
    def __init__(self, gui, pos, size):
        self.gui = gui
        self.pos = pos
        self.size = size
        self.resource_panel = Panel(pos, size, gui)
        self.resource_list = self.get_resource_list()
        self.display = self.resource_list_display()

    def get_resource_list(self):
        resources = []
        for resource in resource_types:
            resources.append(resource)
        return resources


    def resource_list_display(self):
        display = {}
        for i in range(len(self.resource_list)):
            pos = (25,25 + (i*25))
            size = (100,20)
            resource = self.resource_list[i]
            label = pygame_gui.elements.UILabel(container=self.resource_panel.panel,
                                                relative_rect=pg.Rect(pos,size),
                                                manager=self.gui.manager,
                                                text=resource
                                                )
            display[resource] = label
        return display





