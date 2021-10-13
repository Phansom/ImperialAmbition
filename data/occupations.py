OCCUPATIONS = {

    "agriculture": {
        "farmer": {"produces": {"grain": 1.0},
                   "requires": {"farmland": 1.0}
                   },

        "rancher": {"produces":{"meat": 0.65, "leather": 0.2},
                    "requires": {"rangeland": 1.0}
                    },
        "fisher": {"produces":{"fish": 0.85},
                   "requires": {"fishery": 1.0}}
    },

    "extraction": {
        "logger": {"produces":{"wood": 1.0},
                   "requires": {"woodland": 1.0}
                   },
        "excavator": {"produces":{"stone": 0.5},
                      "requires": {"quarry": 1.0}
                      },
        "miner": {"produces":{"metal": 0.5},
                  "requires": {"mine": 1.0}}
    },

    "crafting": {
        "tailor": {
            "produces": {"clothes": 0.5},
            "consumes": {"wool": 1.0},
            "requires": {"industrial": 1.0}
                    },
        "carpenter": {
            "produces": {"furniture": 0.5},
            "consumes": {"wood": 2.0},
            "requires": {"industrial": 1.0}
        },
        "blacksmith": {
            "produces": {"tools": 0.5},
            "consumes": {"metal": 1.0, "wood":0.5},
            "requires": {"industrial":1.0}
        },
        "weaponsmith": {
            "produces": {"weapons": 0.5},
            "consumes": {"metal": 1.0, "leather": 0.25, "wood": 0.25},
            "requires":{"industrial":1.0}
        }
    },

    "mercantile": {
        "trader": {
            "produces": {"local_trade": 1.0},
            "requires": {"commercial": 1.0}},
        "merchant": {
            "produces": {"regional_trade": 1.0},
            "requires": {"commercial": 1.0}}
    },

    "construction":{
        "resource": {
            "produces": {"extraction_capacity": 0.1},
            "consumes": {"materials": 1.0, "land": 1.0}
        },
        "residential": {
            "produces":{"housing_capacity": 0.1},
            "consumes":{"materials": 1.0, "land": 0.5},
        },
        "commercial": {
            "produces":{"mercantile_capacity": 0.075},
            "consumes":{"materials": 1.0, "land": 0.375}
        },
        "industrial": {
            "produces": {"crafting_capacity": 0.05},
            "consumes": {"materials": 1.0, "land": 0.25}
        }
    }
}

