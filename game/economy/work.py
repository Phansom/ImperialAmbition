from dataclasses import dataclass
from data.occupations import OCCUPATIONS
from data.player_city import PLAYER_WORKERS
from .professions import Professions



@dataclass
class Work:
    def __init__(self, economy):
        self.economy = economy
        self.occupations = OCCUPATIONS
        self.professions_list = self.professions_list()
        self.work_data = self.labor_data()

    def professions_list(self):
        professions_list = []
        for occupation in self.occupations:
            professions = self.occupations[occupation]
            if occupation != "construction":
                for profession in professions:
                    professions_list.append(profession)
        return professions_list


    def profession_info(self, occupation_name, profession_name):
        occupation = self.occupations[occupation_name]
        profession = occupation[profession_name]
        return profession


    def workers_in_profession(self, profession):
        num_workers = PLAYER_WORKERS.get(profession)
        return num_workers


    def employed(self):
        employed = 0
        return employed


    def unemployed(self):
        return int(self.economy.population.workers - self.employed())


    def job_capacity(self, profession, business_area):
        land_required_per_worker = profession["requires"]
        max_profession_list = []
        for land_type in land_required_per_worker:
            value_required_per_worker = land_required_per_worker[land_type]
            value = value_required_per_worker * business_area
            max_profession_list.append(value)
        return min(max_profession_list)


    def labor_data(self):
        business = self.economy.business
        pop = self.economy.population.size
        workers = self.economy.population.calc_workers()
        unemployed = self.unemployed()
        occupations = self.occupations
        txt = ""

        for occupation in occupations:
            professions = occupations[occupation]
            for profession in professions:
                if profession in self.professions_list:
                    profession_info = self.profession_info(occupation, profession)
                    requires = profession_info["requires"]
                    for land_type in requires:
                        land_required_per_worker = requires[land_type]
                        land_type_quantity = business.land_size_by_type(land_type)
                        max_workers = land_type_quantity/land_required_per_worker
                        txt += f'{profession}: 0/{int(max_workers)}<br>'
        return txt

