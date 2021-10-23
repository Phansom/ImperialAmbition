from dataclasses import dataclass
# WIP; elements of economy are to be worked in and restructured around this class, before refactoring name to economy


@dataclass
class Business:
    workers: int
    industry: str


@dataclass
class Community:
    population: int


@dataclass
class Location:
    name: str
    actors: dict

    def __init__(self):
        self.actors = actor_data
        self.supply_dict = self.get_actor_data("supply")
        self.demand_dict = self.get_actor_data("demand")


    def get_actor_data(self, data_key):
        data_dict = {}
        actor_d = self.actors[data_key]
        data = actor_d[data_key]
        for item in data:
            value = data[item]
            data_dict[item] = value
        return data_dict


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
print(location.production_dict)


