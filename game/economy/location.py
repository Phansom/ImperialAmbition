from dataclasses import dataclass
from data.starting_data import STARTING_ACTORS, STARTING_RESOURCES
from .community import Community
from .business import Business

# WIP; elements of economy are to be worked in and restructured around this class, before refactoring name to economy


ACTOR_TYPES = {
    "community": Community,
    "business": Business
}


@dataclass
class Location:
    name: str
    actors: dict

    def __init__(self,starting):
        self.name = "Hamlet"
        self.actors = {}
        if starting:
            self.actors = self.generate_starting_actors()
        print(self.actors)


    def generate_starting_actors(self):
        objects = {}
        for actor_type in STARTING_ACTORS:
            actor_data = STARTING_ACTORS[actor_type]
            for actor in actor_data:
                k = actor_data[actor]
                objects[actor] = k
        return objects


    def new_business(self, type, value_dict):
        businesses = self.actors["business"]
        if type in businesses:
            existing_business = businesses[type]
            for data in existing_business:
                value = existing_business[data]
                if value in value_dict:
                    value += value_dict[data]
                    existing_business[data] = value
            return existing_business
        else:
            businesses = self.actors["business"]
            businesses[type] = value_dict
            return businesses
