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
        self.demand = Demand(self)
        self.production = Production(self, self.work.occupations, self.work.professions_list)


    def update(self):
        self.population_demand = self.demand.update()


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


    def update_price(self, resource, demand_met):
        pass


    def update_supply(self):
        supply = {}


    def calc_consumption(self, supply, demand):
        consumption = demand
        for item in consumption:
            if supply[item] < consumption[item]:
                consumption[item] = supply[item]
        return consumption



def anthrome_size(land_size, biome_size):
    return land_size - biome_size

