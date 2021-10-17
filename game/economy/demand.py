from settings import DEMAND_RATE
from .resources import resource_list, default_resource_prices



class Demand:
    def __init__(self, economy):
        self.economy = economy
        self.demand_list = self.calc_demand(economy.population.size, DEMAND_RATE)


    def update(self):
        self.demand_list = self.calc_demand(self.economy.population.size, DEMAND_RATE)


    def calc_demand(self, population_size, demand_rate):
        demand = {}
        for resource in resource_list:
            if resource in demand_rate:
                # TODO calc resource demand here:
                # price of commodity
                # consumer wealth change
                # diminishing marginal utility
                pass
            else:
                demand[resource] = 1

        return demand

    def price_modifier(self, resource):
        original_price = default_resource_prices[resource]
        current_price = self.economy.resource_prices[resource]
        price_modifier = original_price/current_price
        return price_modifier


    def calc_business_demand(self, worker):
        bus_demand = {}
        # this will be used to determine consumption pressure from businesses consuming materials
