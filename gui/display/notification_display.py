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
        self.panel = self.display_panel.panel


    def popup(self, notification):
        buttons = {}
        size = self.main_display.size[0] * 0.5, self.main_display.size[1] * 0.5
        pos = size[0]/2,size[1]/2
        popup_panel = Panel(self.gui,self.main_display,pos,size)
        txt_box = pgui.elements.UITextBox(
            manager = self.gui.manager,
            container = popup_panel.panel,
            relative_rect = pg.Rect((size[0]*0.1, size[1]*0.1),(size[0]*0.75,size[1]*0.75)),
            html_text = notification
        )
        return popup_panel
