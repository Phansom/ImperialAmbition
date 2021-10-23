from dataclasses import dataclass
from data.economics_data import STARTING_ACTORS

# WIP; elements of economy are to be worked in and restructured around this class, before refactoring name to economy



@dataclass
class Business:
    name: str
    workers: int


@dataclass
class Community:
    name: str
    population: int

ACTOR_TYPES = {
    "community": Community,
    "business": Business
}



@dataclass
class Location:
    name: str
    actors: dict

    def __init__(self):
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



    def get_actor_data(self, data_key):
        for actor in self.actors:
            print(actor)


actor_data = {
    "grain_farm":
        {"supply":
             {"grain":4},
         "demand":
             {"labor":1,"farmland":1},
         },
    "sheep_pasture":
        {"supply":
             {"meat":1,"wool":2},
         "demand":
             {"labor":1,"rangeland":1}
         },
    "weaver":
        {"supply":
             {"clothes":1},
         "demand":
             {"labor":1,"wool":3,"industry":1}
        },
    "logger":
        {"supply":
             {"logs":2},
         "demand":
             {"labor":1,"woodland":1}
        },
    "builder":
        {"supply":
             {"structure":0.1},
         "demand":
             {"labor":1,"logs":1}
        }
}

location = Location()
