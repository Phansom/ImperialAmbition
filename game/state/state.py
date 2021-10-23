from dataclasses import dataclass

@dataclass
class State:
    offices = dict



offices = {
    "military tribune": {},
    "legate": {},
    "quaestor": {"minimum age":28},
    "aedile": {"minimum age":35},
    "praetor": {"minimum age":39,
                "imperium":True},
    "consul": {"minimum age":42,
               "imperium":True},
    "censor": {"election interval": 5},
    "tribune of the plebs": {},
    "dictator": {}
}




