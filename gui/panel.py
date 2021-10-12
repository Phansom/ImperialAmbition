import pygame_gui
import pygame as pg

class Panel:
    def __init__(self, pos, size, parent):
        self.pos = pos
        self.size = size
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]),
            container=parent.window,
            manager=parent.manager,
            starting_layer_height=3,
            anchors={'left': 'left',
                     'right': 'left',
                     'top': 'top',
                     'bottom': 'top'
                     })
