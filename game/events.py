import pygame_gui as pgui
import pygame as pg


class Event:
    def __init__(self, game, trigger):
        self.game = game
        self.notification_display = self.game.gui.main_display.notification_display
        self.main_panel = self.game.gui.main_display.main_panel

        if trigger.text in self.toolbar_events():
            self.alert_panel = self.alert_panel()
            self.alert_text(self.alert_panel,"For the republic!")


    def alert_text(self, panel, text):
        pos = (panel.size[0] * 0.05,panel.size[1] * 0.05)
        size = (panel.size[0] * 0.9,panel.size[1] * 0.4)
        txtbox = pgui.elements.UITextBox(container=panel.window,
                                         manager=panel.manager,
                                         relative_rect=pg.Rect(pos,size),
                                         html_text=text)
        return txtbox


    def alert_panel(self):
        container = self.main_panel
        width, height = container.size[0] * 0.6,container.size[1] * 0.8
        x, y = container.size[0] * 0.2,container.size[1] * 0.1
        pos, size = (x, y), (width,height)
        return alert_panel


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
                  "next": self.economy_cycle
                  }

        return events


    def new_game(self):
        location = self.game.economy.generate_starting_location()
        return location


    def load_game(self):
        self.notification_display.print(self.game.economy.to_text())


    def economy_cycle(self):
        if self.game.economy is None:
            return "There is no Economy object!"
        self.game.economy.update()
        display_text = self.game.economy.to_text()
        return self.game.gui.main_display.notification_display.print(display_text)
