from data.player_city import PLAYER_POPULATION
from settings import AGE_RATES, AGE_GROUPS


class Population:
    def __init__(self):
        self.size = PLAYER_POPULATION["size"]
        self.age_groups = self.set_age_groups()
        self.age_data = self.generate_age_data()
        self.workers = self.calc_workers()

    def pop_data(self):
        pop_data = {"size": self.size,
                    "workers": self.workers,
                    "age_data": self.age_data,
                    }
        return pop_data


    def generate_age_data(self):
        age_rates, age_dict, size, actual_size = AGE_RATES, {}, self.size, 0
        for age in age_rates:
            age_rate = age_rates[age]
            age_dict[age] = int(age_rate * self.size)
            actual_size += age_dict[age]
        age_dict[0] += (self.size - actual_size)
        return age_dict


    def set_age_groups(self):
        age_groups = {}
        for age_group in AGE_GROUPS:
            ages = AGE_GROUPS[age_group]
            for age in ages:
                age_groups[age] = age_group
        return age_groups


    def calc_workers(self):
        workers = 0
        for age in self.age_data:
            age_group = self.age_groups[age]
            if age_group == "adult":
                workers += self.age_data[age]
        return workers