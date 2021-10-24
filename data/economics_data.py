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



