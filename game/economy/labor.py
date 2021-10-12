from dataclasses import dataclass
from data.occupations import OCCUPATIONS
from .professions import Professions


@dataclass
class Labor:
    def __init__(self, economy):
        self.economy = economy
        self.occupations = occupations()
        self.labor_data = self.labor_data()
        self.agriculture_data = Professions(self.occupations, economy)

    employed: int = 0
    population: int = 1000
    workforce_rate: float = 0.5


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
        CURRENT_FARMERS = 0
        CURRENT_LOGGERS = 0
        business = self.economy.business
        pop = self.population
        workforce = self.workforce()
        unemployed = self.unemployed()

        farmland = business.land_size_by_type("farmland")
        farmer_info = self.profession_info("agriculture", "farmer")
        farmer_capacity = int(self.job_capacity(farmer_info, farmland))
        farmers = CURRENT_FARMERS

        woodland = business.land_size_by_type("woodland")
        logger_info = self.profession_info("extraction", "logger")
        logger_capacity = int(self.job_capacity(logger_info, woodland))
        loggers = CURRENT_LOGGERS


        pos = (25, 25)
        txt = f'population : {pop}  <br>' \
              f'workforce  : {workforce}<br>' \
              f'unemployed : {unemployed}<br>'\
              f' <br>' \
              f'farmers    : {farmers}/{farmer_capacity}<br>' \
              f'loggers    : {loggers}/{logger_capacity}<br>'
        size = (-1,-1)
        return txt


def occupations():
    occupations = OCCUPATIONS
    return occupations



