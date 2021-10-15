from .land import Land
from .work import Work
from settings import DEMAND_RATE
from .resources import *
from .production import Production
from .population import Population
from .demand import Demand



class Economy:
    def __init__(self, game):
        self.game = game
        self.population = Population()
        self.business = Land()
        self.work = Work(self)
        self.production = Production(self, self.work.occupations, self.work.professions_list)
        self.demand = Demand(self)
        self.supply = self.production.production_list
        self.resource_prices = default_resource_prices

    def update(self):
        self.demand.update()
        self.production.update(self, self.work.occupations, self.work.professions_list)
        self.resource_prices = self.update_resource_prices(self.resource_prices)


    def get_player_resource_data(self, resource):
        type = get_resource_type(resource)
        storage = get_resource_count(resource)
        production = get_resource_production(self.production.production_list, resource)

        consumption = {}

        resource_data = {
            "type": type,
            "storage": storage,
            "production": production,
            "consumption": consumption
        }
        return resource_data


    def calc_consumption(self, supply, demand):
        consumption = demand
        for item in consumption:
            if supply[item] < consumption[item]:
                consumption[item] = supply[item]
        return consumption

    def update_resource_prices(self, resource_prices):
        prd_list = self.production.production_list
        demand_list = self.demand.demand_list
        new_resource_prices = {}

        for resource in resource_prices:

            supply, demand = 1, 1
            if resource in prd_list:
                supply = prd_list[resource]
            if resource in demand_list:
                demand = demand_list[resource]

            old_price = resource_prices[resource]
            trend_mult = self.trending_multiplier(supply,demand)
            trending = self.trending_price(old_price, trend_mult)
            new_price = self.resource_price_change(trending, old_price)
            new_resource_prices[resource] = new_price

            if resource == "grain":
                print(f'''resource: {resource}
                old_price: {old_price}
                new_price: {new_price}
                trending: {trending}
                multiplier: {trend_mult}
                ''')

        return new_resource_prices



    def resource_price_change(self, trending, current):
        new_price = (trending/current - 1)/2 * current + current
        return new_price


    def trending_multiplier(self, supply, demand):
        if supply == 0:
            supply = 1
        if demand == 0:
            demand = 1
        trending_multiplier = demand/supply
        return trending_multiplier


    def trending_price(self, current_price, trending_multiplier):
        trending_price = current_price * trending_multiplier
        return trending_price



def anthrome_size(land_size, biome_size):
    return land_size - biome_size

