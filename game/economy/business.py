from dataclasses import dataclass
from data.player_city import PLAYER_CITY

@dataclass
class Business:
    def __init__(self):
        self.player_city = PLAYER_CITY
        self.total_land = self.player_city["max_land"]

        self.used_land_list = self.used_land_list()
        self.business_data = self.business_data()


    business_area = float
    business_area_types = ["farmland","rangeland","fishery","woodland","quarry","mine","industrial","commercial",
                           "residential"]
    business_area_makeup = {}

    def business_data(self):
        print(self.used_land())
        print(self.total_land)
        business_data = f'<br>LAND: {self.total_land}'
        return business_data


    def land_size_by_type(self, type):
        if type in self.used_land_list:
            type_size = self.used_land_list[type]
            return type_size


    def remaining_land(self):
        used_land = self.used_land()
        max_land = self.player_city["max_land"]
        return max_land - used_land

    def used_land_list(self):
        land = self.player_city
        used_land_list = {}
        for entry in land:
            if entry != "max_land":
                used_land_list[entry] = land[entry]
        return used_land_list

    def used_land(self):
        land = self.player_city
        used_land = 0
        for entry in land:
            if entry != "max_land":
                land_used_by_type = land[entry]
                used_land += land_used_by_type
        return used_land



