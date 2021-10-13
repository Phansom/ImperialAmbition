

class Professions:
    def __init__(self, occupation, occupations, economy):
        self.economy = economy
        self.land_data = economy.business.used_land_list

        agriculture_data = occupations["agriculture"]
        #print(self.max_profession(agriculture_data, "farmer"))


    def max_profession(self, occupation, profession):
        used_land = occupation[profession]['requires']
        land_type = None
        for entry in used_land:
            land_type = entry
        if land_type is not None:
            land = self.economy.business.land_size_by_type(land_type)
            land_per_worker = used_land[land_type]
            max_workers = int(land * land_per_worker)
            return max_workers

