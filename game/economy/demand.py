from settings import DEMAND_RATE

class Demand:
    def __init__(self, economy):
        self.economy = economy
        self.demand_list = self.calc_population_demand(economy.population.size, DEMAND_RATE)


    def update(self):
        self.demand_list = self.calc_population_demand(self.economy.population.size, DEMAND_RATE)


    def calc_population_demand(self, population_size, demand_rate):
        pop_demand = {}
        for good in demand_rate:
            total_required = demand_rate[good] * population_size
            pop_demand[good] = total_required
        return pop_demand


    def calc_business_demand(self, worker):
        bus_demand = {}
        # this will be used to determine consumption pressure from businesses consuming materials
