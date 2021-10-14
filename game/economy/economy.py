from .business import Business
from .labor import Labor
from settings import DEMAND_RATE
from data.player_city import PLAYER_WORKERS, PLAYER_RESOURCES
from .resources import *



class Economy:
    def __init__(self, game):
        self.game = game
        self.business = Business()
        self.labor = Labor(self)
        self.demand = self.calc_population_demand(self.labor.population, DEMAND_RATE)
        self.production = self.calc_production(self.labor.occupations, self.labor.professions_list)

        print(get_type_production(self.production, "food"))

    population = int
    land_size = float
    biome_size = float

    def calc_population_demand(self, population, demand_rate):
        demand = {}
        for good in demand_rate:
            total_required = demand_rate[good] * population
            demand[good] = total_required
        return demand


    def calc_production(self, occupations, professions_list):
        goods_produced = {}

        for occupation in occupations:
            professions = occupations[occupation]

            for profession in professions:

                if profession in professions_list:
                    profession_info = self.labor.profession_info(occupation, profession)
                    produce_per_worker = profession_info["produces"]

                    for good_produced in produce_per_worker:
                        amount_per_worker = produce_per_worker[good_produced]
                        num_workers = self.workers_in_profession(profession)
                        amount_produced = 0

                        if num_workers != None:
                            amount_produced = num_workers * amount_per_worker

                        if good_produced in goods_produced:
                            goods_produced[good_produced] += amount_produced
                        else:
                            goods_produced[good_produced] = amount_produced

        return goods_produced

    def workers_in_profession(self, profession):
        num_workers = PLAYER_WORKERS.get(profession)
        return num_workers

    def resource_data_txt(self):
        txt = "<b><u>Resource Storage:</u></b><br>"
        for resource_type in PLAYER_RESOURCES:
            resources = PLAYER_RESOURCES[resource_type]
            for resource in resources:
                storage = resources[resource]
                for item in storage:
                    txt += f"{resource}: {storage[item]}<br>"
        return txt

    def production_data_txt(self):
        txt = ""
        for good in self.production:
            txt += f"{good}: {self.production[good]}<br>"
        return txt

    def get_player_resource_data(self, resource):
        type = get_resource_type(resource)
        storage = get_resource_count(resource)
        production = get_resource_production(self.production, resource)

        # TODO: GET GET_RESOURCE_CONSUMPTION TO WORK. RIGHT NOW MORE TIED TO TYPE THAN RESOURCE.
        # TIME TO START WORKING ON ECONOMY INTERACTIONS. HoooOOray!~
        consumption = {}

        resource_data = {
            "type": type,
            "storage": storage,
            "production": production,
            "consumption": consumption
        }
        return resource_data


def anthrome_size(land_size, biome_size):
    return land_size - biome_size


ANTHROMES = {
    "farmland": "farm",
    "woodland": "logging",
    "rangeland": "pasture"
}



