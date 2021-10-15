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
        self.pop_data = self.economy.population.pop_data()
        self.work_data = self.economy.work.work_data
        self.business_data = self.economy.business.business_data

        self.data_display_txt = self.data_display_txt_home()
        self.pop_data_txt = self.pop_data_txt(self.pop_data)
        self.data_display = self.main_data_display(self.data_display_txt)
        self.data_buttons = self.data_buttons()
        self.buttons_dict = self.buttons_list_to_dict(self.data_buttons)

    def change_main_display(self, button_text):
        self.data_display.kill()
        display_txt = self.load_button_text_data(button_text)
        self.main_data_display(display_txt)


    def data_display_txt_home(self):
        demand_data = self.economy.demand.demand_list
        production_list = self.economy.production.production_list
        demand = 0

        txt = "<u>DATA DISPLAY HOME</u><br>"
        txt += " <br><b>Resource: Stored (Supply/Demand):</b><br>"
        for resource in production_list:
            stored = self.economy.get_player_resource_data(resource)["storage"]
            if resource in demand_data:
                demand = int(demand_data[resource])
            supply = int(production_list[resource])

            txt += f'{resource}: {stored} ({supply}/{demand})<br>'

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
            'pop': self.pop_data_txt,
            'work': self.work_data,
            'land':self.business_data,
            'update': self.economy.update()
        }.get(button_text, "The data wasn't found! Check MainDisplay.load_button_text_data.")


    def buttons_list_to_dict(self, buttons_list):
        data_button_names = DATA_BUTTON_NAMES
        buttons_dict = {}
        for i in range(len(buttons_list)):
            buttons_dict[data_button_names[i]] = buttons_list[i]
        return buttons_dict


    def pop_data_txt(self, pop_data):
        txt = f"Population: {pop_data['size']}<br>Workers: {pop_data['workers']}"

        return txt






