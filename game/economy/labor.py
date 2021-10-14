from dataclasses import dataclass
from data.occupations import OCCUPATIONS
from .professions import Professions


@dataclass
class Labor:
    def __init__(self, economy):
        self.economy = economy
        self.occupations = OCCUPATIONS
        self.professions_list = self.professions_list()
        self.labor_data = self.labor_data()

    employed: int = 0
    population: int = 1000
    workforce_rate: float = 0.5

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


    def workforce(self):
        return int(self.population * self.workforce_rate)


    def unemployed(self):
        return int(self.workforce() - self.employed)


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
        pop = self.population
        workforce = self.workforce()
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

