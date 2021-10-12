from .business import Business
from .labor import Labor


class Economy:
    def __init__(self, game):
        self.game = game
        self.business = Business()
        self.labor = Labor(self)

    population = int
    land_size = float
    biome_size = float


    def production(self):
        pass


def anthrome_size(land_size, biome_size):
    return land_size - biome_size


ANTHROMES = {
    "farmland": "farm",
    "woodland": "logging",
    "rangeland": "pasture"
}



