import random
from data.population_data import POSSIBLE_GENS
from data.resource_data import RESOURCES
from data.economics_data import ACTORS, DEMAND
from settings import STARTING_COMMUNITIES, BASE_COMMUNITY_SIZE, DEFAULT_COMMUNITIES
from util import find_key_parent
from game.economy.community import Community


# ECON MAY BE REPLACING THIS WHOLESALE


class Economy:
    def __init__(self):
        self.available_gens = POSSIBLE_GENS
        self.demand_types = list(DEMAND)
        self.active_communities = self.setup_communities()



    def print(self):
        return f'There are {self.workforce_size()} workers.'


    def update(self):
        pass


    def workforce_size(self):
        workforce = 0
        for community in self.active_communities:
            workforce += self.active_communities[community].provided_labor()
        return workforce


    def get_community(self, gens):
        return self.active_communities[gens]


    def setup_economy(self):
        active_communities = self.setup_communities()
        return active_communities


    def setup_communities(self):
        active_communities = {}
        for i in range(DEFAULT_COMMUNITIES):
            community = self.new_community()
            active_communities[community.gens] = community
        return active_communities


    def new_community(self):
        gens = random.choice(POSSIBLE_GENS)
        members = random.randint(100, 200)
        self.available_gens.remove(gens)
        community = Community(gens=gens, members=members)
        return community


    def return_resource_list(self):
        resource_list = []
        for category in RESOURCES:
            types = RESOURCES[category]
            for type in types:
                resources = types[type]
                for resource in resources:
                    resource_list.append(resource)
        return resource_list


    def return_actors(self):
        actor_list = []
        for actor in ACTORS:
            actor_list.append(actor)
        return actor_list


    def return_resource_categories(self):
        categories = []
        for category in RESOURCES:
            categories.append(category)
        return categories


    def find_type_category(self, resource_type):
        category = find_key_parent(RESOURCES, resource_type)
        return category


    def return_resource_types(self):
        resource_types = []
        for category in RESOURCES:
            types = RESOURCES[category]
            for type in types:
                resource_types.append(type)
        return resource_types



economy = Economy()


