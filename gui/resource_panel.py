from gui.panel import Panel
from settings import RESOURCE_HEADER_NAMES
from game.economy.economy import resource_list
import util

class ResourcePanel:
    def __init__(self, gui, pos, size):
        self.gui = gui
        self.pos = pos
        self.size = size
        self.resource_list = resource_list
        self.resource_panel = Panel(pos, size, gui)
        self.display = self.resource_display(self.resource_panel.panel)

    def update(self):
        self.display = self.resource_display(self.resource_panel)


    def resource_display(self, panel):
        headers = self.generate_headers(panel)
        names = self.resource_names_display(panel)
        supply = self.supply_display(panel)
        demand = self.demand_display(panel)

        display = {
            "headers": headers,
            "names": names,
            "supply": supply,
            "demand": demand
        }

        return display

    def resource_names_display(self, panel):
        display = {}
        for i in range(len(self.resource_list)):
            pos = (20,55 + (i*35))
            size = (100,35)
            resource = self.resource_list[i]
            label = util.new_label(panel,self.gui.manager,pos,size,resource)
            display[resource] = label
        return display


    def supply_display(self, panel):
        display = {}
        for i in range(len(self.resource_list)):
            pos = (120, 55 + (i * 35))
            size = (100, 35)
            resource = self.resource_list[i]
            supply = str(int(self.gui.game.economy.supply.supply_list[resource]))

            label = util.new_label(panel, self.gui.manager, pos, size, supply)
            display[resource] = label
        return display

    def demand_display(self, panel):
        display = {}
        for i in range(len(self.resource_list)):
            pos = (220, 55 + (i * 35))
            size = (100, 35)
            resource = self.resource_list[i]
            # TODO placeholder
            demand = "DEMAND"

            label = util.new_label(panel, self.gui.manager, pos, size, demand)
            display[resource] = label
        return display


    def generate_headers(self, container):
        headers = {}
        x, y = 20,20
        for i in range(len(RESOURCE_HEADER_NAMES)):
            pos = (x + (i*100),20)
            size = (100,35)
            name = RESOURCE_HEADER_NAMES[i]
            headers[name] = util.new_header(self.resource_panel.panel, self.gui.manager, pos, size, name)
        return headers

