# RESOURCES -> GOODS AND SERVICES
# BIGGER/MORE COMPLEX REQUIRE MORE RESOURCES
# TYPES OF RESOURCES: NATURAL RESOURCES, HUMAN RESOURCES, and CAPITAL GOODS

AGE_RATES = {0: 0.23248,
             1: 0.18598,
             2: 0.15499,
             3: 0.13949,
             4: 0.11655,
             5: 0.09299,
             6: 0.06199,
             7: 0.01549}

AGE_GROUPS = {
    "adolescent":{0,1},
    "adult":{2,3,4,5},
    "senior":{6,7}
}

ACTORS = {
    "household",
    "business",
    "state",
    "societal"
}

DEMAND = {
    "life": {
        "food",
        "water",
        "shelter"},
    "needs": {
        "food",
        "water",
        "shelter",
        "clothing"},
    "wants": {
        "luxury",
        "entertainment",
        "spirituality"
    },
    "security": {
        "safety",
        "livelihood",
        "goods",
        "health",
        "justice"},
    "social": {
        "family",
        "friends",
        "tribe"},
    "esteem": {
        "achievement",
        "respect",
        "freedom"},
    "self-actualization": {
        "morality",
        "leadership",
        "prejudice",
        "expression",
        "creativity"
    }
}

SUPPLY = {
    "production": {},
    "imports": {},
}

RESOURCES = {
    "natural": {"land": {
        "area","value", "arability"
    },"hydro": {
        "fresh_water","river_connectivity","port_access"
    },"mineral": {
        "iron", "coal", "gold", "stone"
    }},

    "human": {"labor": {
        "unskilled","specialized"
    }, "time": {
        "duration", "quality"
    }},

    "capital":{"factory": {
        "agriculture","extraction","commercial","production"
    },"tools": {
        "basic","logistical","industrial"
    }}
}

GOOD_CATEGORIES = {
    "private",
    "public",
    "common",
    "club"
}

PUBLIC_RESOURCES = ["land", "hydro", "mineral"]
PRIVATE_RESOURCES = ["labor", "factory", "tools"]

STARTING_RESOURCES = {
    "land": {"makeup":{
                 "biome":{
                     "grassland":600,
                     "forest":250,
                     "aquatic":0,
                     "desert":0,
                     "tundra":0
                    },
                 "anthrome": {
                     "urban":5,
                     "suburban":15,
                     "farmland":40,
                     "woodland":40,
                     "rangeland":25,
                     "wildland":25
                    }
                },
             "suitability": {
                 "farmland": 1.0,
                 "woodland": 0.9,
                 "rangeland": 1.0,
                 "wildland": 0.7
                }
             }
}


STARTING_ACTORS = {
    "community": {"Julia": {
        "population": 100,
        "private_resources": {
        }
    }, "Octavia": {
        "population": 80,
        "private_resources": {}
    }},
}




POSSIBLE_GENS = ["Aemilia",
                 "Aebutia",
                 "Antonia",
                 "Aquillia",
                 "Atilia",
                 "Caecilia",
                 "Calpurnia",
                 "Cassia",
                 "Claudia",
                 "Cornelia",
                 "Curtia",
                 "Domitia",
                 "Fabia",
                 "Fulvia",
                 "Furia",
                 "Gregania",
                 "Genucia",
                 "Horatia",
                 "Hostilia",
                 "Julia",
                 "Junia",
                 "Licinia",
                 "Lucretia",
                 "Manlia",
                 "Marcia",
                 "Menenia",
                 "Metilia",
                 "Minucia",
                 "Mucia",
                 "Nautia",
                 "Octavia",
                 "Oppia",
                 "Papiria",
                 "Pinaria",
                 "Plautia",
                 "Pompeia",
                 "Pomponia",
                 "Popillia",
                 "Porcia",
                 "Postumia",
                 "Quinctia",
                 "Scribonia",
                 "Sempronia",
                 "Sergia",
                 "Servilia",
                 "Sextilia",
                 "Sulpicia",
                 "Terentia",
                 "Titia",
                 "Tulia",
                 "Valeria",
                 "Verginia",
                 "Veturia",
                 "Vibia",
                 "Volumnia"]



