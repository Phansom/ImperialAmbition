import pygame as pg
import pygame_gui as pgui
from gui.gui import Gui
import sys
from .events import Event
from .economy.economy import Economy

class Game:

    def __init__(self, window_surface, background, clock):
        self.window_surface = window_surface
        self.background = background
        self.clock = clock
        self.width, self.height = self.window_surface.get_size()
        self.manager = pgui.UIManager((self.width, self.height))
        self.gui = Gui(self, self.manager, window_surface)
        self.economy = Economy()


    def run(self, time_delta):
        self.events()
        self.update(time_delta)
        self.draw()


    def update(self, time_delta):
        self.manager.update(time_delta)
        pg.display.update()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_SPACE:
                    pass
            if event.type == pg.USEREVENT:
                if event.user_type == pgui.UI_BUTTON_PRESSED:
                    triggered_event = Event(self, event.ui_element)
            self.manager.process_events(event)


    def draw(self):
        self.window_surface.blit(self.background, (0,0))
        self.manager.draw_ui(self.window_surface)


    def save(self,save_name, save_data):
        f = open(f"{save_name}.txt","w")
        f.write(save_data)
        f.close()

    def load(self, save_name):
        f = open(f"{save_name}.txt","r")
        print(f.read())



