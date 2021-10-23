import pygame_gui as pgui
import pygame as pg


class Event:
    def __init__(self, game, trigger):
        self.game = game
        self.notification_display = self.game.gui.main_display.notification_display
        self.main_panel = self.game.gui.main_display.main_panel

        if trigger.text in self.toolbar_events():
            events = self.toolbar_events()
            event = events[trigger.text]
            event()
            self.notification_pin = self.new_notification_pin(trigger)


    def new_notification_pin(self, trigger):
        container_size = self.notification_display.size
        w, h = container_size[0] * 0.9, container_size[1] * 0.05
        x, y = container_size[0] * 0.03, container_size[1] * 0.008
        pos, size = (x,y), (w,h)

        button = pgui.elements.UIButton(
            manager=self.game.manager,
            container=self.notification_display.panel,
            relative_rect=pg.Rect(pos,size),
            text = trigger.text,
        )
        return button


    def toolbar_events(self):
        events = {"new": self.new_game,
                  "load": self.load_game,
                  "next": self.economy_cycle}

        return events


    def new_game(self):
        pass



    def load_game(self):
        print("load_game")
        return "load_game"


    def economy_cycle(self):
        if self.game.economy is None:
            return "There is no Economy object!"
        self.game.economy.update()
        display_text = self.game.economy.print()
        return self.game.gui.main_display.notification_display.popup(display_text)
