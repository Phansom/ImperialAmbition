from game.economy.economy import *


class Supply:
    def __init__(self, economy, occupations, professions_list):
        self.economy = economy
        self.occupations = occupations
        self.professions_list = professions_list
        self.supply_list = self.calc_supply()


    def update(self):
        self.supply_list = self.calc_supply()


    def update_supply(self):
        pass


    def calc_supply(self):
        supply = self.calc_production()
        return supply


    def calc_production_group(self, type):
        production = 0
        for product in self.supply_list:
            product_type = get_resource_type(product)
            if product_type == type:
                production += self.supply_list[product]
        return production


    def calc_production(self):
        economy, occupations, professions_list = self.economy, self.occupations, self.professions_list
        goods_produced = {}

        for occupation in occupations:
            professions = occupations[occupation]

            for profession in professions:

                if profession in professions_list:
                    profession_info = economy.work.profession_info(occupation, profession)
                    produce_per_worker = profession_info["produces"]

                    for good_produced in produce_per_worker:
                        amount_per_worker = produce_per_worker[good_produced]
                        num_workers = economy.work.workers_in_profession(profession)
                        amount_produced = 0

                        if num_workers != None:
                            amount_produced = num_workers * amount_per_worker

                        if good_produced in goods_produced:
                            goods_produced[good_produced] += amount_produced
                        else:
                            goods_produced[good_produced] = amount_produced

        return goods_produced

    # TODO: start implementing supply formulas.
    def linear_supply(self):
        aggregate_supply = "the total quantity of output"
        qty_supplied = min_supplied + price_coefficient(market_price)

        pass
