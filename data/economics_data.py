import dataclasses
from dataclasses import dataclass
from data.resource_data import resource_list, default_resource_prices, base_demand, resource_types
import game.economy.resources


class EconomicsData:
    def __init__(self):
        self.prices = self.new_dict(resource_list, self.get_price)
        self.demand = Demand(base_demand, resource_list, goods, services)
        print(self.prices)



    def new_dict(self, key_list, value_method):
        dict = {}
        for i in range(len(key_list)):
            key = key_list[i]
            value = value_method(key)
            dict[key] = value
        return dict

    def get_hierarchy_level(self):
        for resource in resource_list:
            self.get_type(resource)
            if type == "food":
                return "survival"




    def get_price(self, k):
        return default_resource_prices[k]


    def get_type(self, k):
        return resource_types[k]


# GOAL OF THIS CLASS IS TO RETURN A "RESOURCE" INSTANCE
@dataclass
class Resource:
    name: str
    type: str
    amount: float



# GOAL OF THIS CLASS IS TO RETURN A "DEMAND" DICT (DEMAND # FOR EVERY RESOURCE)
@dataclass
class Demand:
    hierarchy: dict
    resources: dict
    goods: list
    services: list
