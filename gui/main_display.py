import pygame as pg
import pygame_gui as pgui
from .panel import Panel

class MainDisplay:
    def __init__(self, gui, loc, size):
        self.gui = gui
        self.loc = loc
        self.size = (size[0] * 0.9, size[1] * 0.9)
        self.pos = (size[0] * 0.05, size[1] * 0.05)
        self.main_panel = Panel(self.pos, self.size, self.gui)
        self.economy = self.gui.game.economy
        self.labor_data = self.economy.labor.labor_data
        self.business_data = self.economy.business.business_data
        self.pop_data_display(self.size)


    def pop_data_display(self, size):
        txt = f'{self.labor_data}<br>' \
              f'<br>' \
              f'{self.business_data}<br>'

        x = 10
        y = 10
        width = (size[0] * 0.5) - 20
        height = size[1] - 25

        pop_data_display = pgui.elements.UITextBox(
            html_text= str(txt),
            manager = self.gui.manager,
            container = self.main_panel.panel,
            relative_rect= pg.Rect((x,y),(width,height))
        )
        return pop_data_display





