from dataclasses import dataclass
from settings import AGE_RATES, AGE_GROUPS, DESIRED_HOUSEHOLD_SIZE

@dataclass
class Community:
    def __init__(self, gens, members):
        self.gens = gens
        self.members = members
        self.children = self.get_age_count("adolescent")
        self.adults = self.get_age_count("adult")
        self.seniors = self.get_age_count("senior")
        self.desired_households = int(self.get_housing_demand())


    def print(self):
        return f'{self.gens}: {self.members} members.\n' \
               f'There are {self.desired_households} heads of household.\n' \
               f'These households provide {self.provided_labor()} labor.'


    def get_housing_demand(self):
        return self.members/DESIRED_HOUSEHOLD_SIZE


    def get_age_count(self, age_group):
        group_size = 0
        for entry in AGE_RATES:
            if entry in AGE_GROUPS[age_group]:
                multiplier = AGE_RATES[entry]
                group_size += (multiplier * self.members)
        return int(group_size)

    def provided_labor(self):
        return self.adults

