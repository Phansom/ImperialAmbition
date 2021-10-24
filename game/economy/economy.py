from .location import Location

class Economy:
    def __init__(self):
        self.locations = {}

    def generate_starting_location(self):
        location = Location(starting=True)
        self.locations[location.name] = location
        return location

    def update(self):
        pass

    def to_text(self):
        locations_text = ""
        for element in self.locations:
            location = self.locations[element]
            locations_text += f"{location.name}"
        return locations_text


