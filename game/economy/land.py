from dataclasses import dataclass
from data.player_city import PLAYER_LAND

@dataclass
class Land:
    def __init__(self):
        self.player_land = PLAYER_LAND
        self.total_land = self.player_land["max_land"]

        self.used_land_list = self.player_anthrome_list()
        self.business_data = self.business_data()


    business_area = float
    business_area_types = {"farmland": "farmer",
                           "rangeland": "rancher",
                           "fishery": "fisher",
                           "woodland": "logger",
                           "quarry": "excavator",
                           "mine":"miner",
                           "industrial":"craftsman",
                           "commercial":"trader"}


    def business_data(self):
        business_data = f'<b><u>land       : {self.total_land}</u></b><br>' \
                        f'biomes     : {self.player_biome_size()}<br>' \
                        f'anthromes  : {self.player_anthrome_size()}'

        return business_data


    def land_size_by_type(self, type):
        if type in self.used_land_list:
            type_size = self.used_land_list[type]
            return type_size


    def player_anthrome_list(self):
        land = self.player_land
        used_land_list = {}
        for entry in land:
            if entry != "max_land":
                used_land_list[entry] = land[entry]
        return used_land_list


    def player_anthrome_size(self):
        land = self.player_land
        used_land = 0
        for entry in land:
            if entry != "max_land":
                land_used_by_type = land[entry]
                used_land += land_used_by_type
        return used_land


    def player_biome_size(self):
        used_land = self.player_anthrome_size()
        max_land = self.player_land["max_land"]
        return max_land - used_land



