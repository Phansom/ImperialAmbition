from dataclasses import dataclass


class Production:
    def __init__(self):
        self.factories = {}
        self.factory_id = 1


    def total_jobs(self, factories):
        jobs = 0
        for factory in factories:
            jobs += factory.labor_demand
        return jobs


    def new_factory(self):
        factory = self.Factory()
        self.factories[self.factory_id] = factory
        self.factory_id += 1
        return factory


    @dataclass
    class Factory:
        id = int
        type = str
        labor_demand = int
        labor_supplied = int
        resources_demanded = dict
        goods_produced = dict

        def labor_satisfaction(self, supply, demand):
            if supply > demand:
                return 1
            if demand > supply:
                return supply/demand







