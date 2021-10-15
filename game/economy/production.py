from game.economy.resources import *


class Production:
    def __init__(self, economy, occupations, professions_list):
        self.production_list = self.calc_production(economy, occupations, professions_list)


    def update(self, economy, occupations, professions_list):
        self.production_list = self.calc_production(economy, occupations, professions_list)


    def calc_production_group(self, type):
        production = 0
        for product in self.production_list:
            product_type = get_resource_type(product)
            if product_type == type:
                production += self.production_list[product]
        return production


    def calc_production(self, economy, occupations, professions_list):
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


