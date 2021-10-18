from settings import DEMAND_RATE
from .resources import resource_list, default_resource_prices



class Demand:
    def __init__(self, economy):
        self.economy = economy
        self.demand_list = self.init_demand_list()


    def init_demand_list(self):
        demand_list = {}
        for resource in resource_list:
            demand_list[resource] = 0
        return demand_list

