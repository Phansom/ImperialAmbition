from dataclasses import dataclass
from game.economy.community import Community

@dataclass
class Character:
    name: str
    community: Community



# Every Character has a name.
# Every character belongs to a community (which has its own information).
