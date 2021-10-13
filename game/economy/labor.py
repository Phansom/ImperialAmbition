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
        self.total_job_capacity = self.total_job_capacity()



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


    def total_job_capacity(self):
        total_job_capacity = 0


        return total_job_capacity


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
                        print(f'{land_type}: {land_required_per_worker}')



            # for profession in professions[occupation_name]:
            #     profession_name = profession
            #     land_type = business.land_size_by_type("farmland")
            #     profession_info = self.profession_info(occupation_name, profession_name)
            #     profession_capacity = int(self.job_capacity(profession_info, land_type))
            #     txt += f'{profession_capacity}<br>'

        # txt = f'<b><u>population : {pop}</u></b><br>' \
        #       f'workforce  : {workforce}<br>' \
        #       f'unemployed : {unemployed}<br>'\
        #       f' <br> <br>' \
        #       f'<b><u>employed   : {self.employed}/{self.total_job_capacity}</u></b><br>' \
        #       f'farmers    : {0}/{farmer_capacity}<br>'
        return txt


