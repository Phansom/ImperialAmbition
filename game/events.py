import pygame_gui as pgui
import pygame as pg
from .economy.economy import Economy

class Event:
    def __init__(self, game, trigger):
        self.game = game
        self.notif_panel = self.game.gui.main_display.notification_panel
        self.main_panel = self.game.gui.main_display.main_panel
        events = {
            "new": new_game(game),
            "load": load_game(),
            "next": economy_cycle()
        }
        if trigger in self.game.gui.main_display.toolbar_elements:
            event = events[trigger.text]

        container_size = self.notif_panel.size
        w, h = container_size[0] - 30, container_size[1] * 0.05
        x, y = 10, 10
        pos, size = (x,y), (w,h)
        self.notification_pin = self.new_notification_pin(trigger,pos,size)


    def new_notification_pin(self, trigger, pos, size):
        button = pgui.elements.UIButton(
            text=trigger.text,
            manager=self.game.manager,
            relative_rect=pg.Rect(pos,size),
            container=self.notif_panel.panel

        )
        return button


    def trigger_notification_pin(self):
        self.display_notification()


    def display_notification(self):
        text_box = pgui.elements.UITextBox(
            html_text="text goes here",
            manager = self.game.manager,
            relative_rect = pg.Rect((10,10),(-1,-1)),
            container=self.main_panel.panel
        )
        return text_box




def new_game(game):
    game.economy = Economy()
    return game.economy.print()

def load_game():
    return "load_game"

def economy_cycle():
    return "economy_cycle"
