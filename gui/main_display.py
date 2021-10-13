import pygame as pg
import pygame_gui as pgui
from .panel import Panel
from settings import DATA_BUTTON_NAMES

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

        self.data_display_txt = self.data_display_txt_home(self.labor_data, self.business_data)
        self.data_display = self.main_data_display(self.data_display_txt)
        self.data_buttons = self.data_buttons()
        self.buttons_dict = self.buttons_list_to_dict(self.data_buttons)

    def change_main_display(self, button_text):
        self.data_display.kill()
        button = self.get_data_button(button_text)
        display_txt = self.load_button_text_data(button_text)
        self.main_data_display(display_txt)



    def data_display_txt_home(self, labor, business):
        txt = f'{labor}<br>' \
              f' <br> <br>' \
              f'{business}<br>'
        return txt


    def get_data_button(self, name):
        return self.buttons_dict[name]

    def main_data_display(self, txt):
        size = self.size
        x = (size[0] * 0.035)
        y = (size[1] * 0.005)
        width = (size[0] * 0.2)
        height = (size[1] * 0.4)

        data_display = pgui.elements.UITextBox(
            html_text= str(txt),
            manager = self.gui.manager,
            container = self.main_panel.panel,
            relative_rect= pg.Rect((x,y),(width, height))
        )
        return data_display

    def data_buttons(self):
        size = self.size
        elements = DATA_BUTTON_NAMES
        buttons = []
        for i in range(len(elements)):
            width = (size[0] * 0.03)
            height = width
            spacing = (height/10)
            x = spacing
            y = spacing + (i * (height + spacing))
            element = elements[i]
            button = pgui.elements.UIButton(
                text = element,
                manager = self.gui.manager,
                container=self.main_panel.panel,
                relative_rect = pg.Rect((x,y),(width,height))
            )
            buttons.append(button)
        return buttons

    def load_button_text_data(self, button_text):
        return {
            'pop': self.economy.labor.professions_list,
            'work':self.labor_data,
            'land':self.business_data
        }.get(button_text, "The data wasn't found!")


    def buttons_list_to_dict(self, buttons_list):
        data_button_names = DATA_BUTTON_NAMES
        buttons_dict = {}
        for i in range(len(buttons_list)):
            buttons_dict[data_button_names[i]] = buttons_list[i]
        return buttons_dict







