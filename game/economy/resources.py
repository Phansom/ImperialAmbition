from data.player_city import PLAYER_RESOURCES

def get_resource_type(resource):
    for type in resource_types:
        resources_of_type = resource_types[type]
        for item in resources_of_type:
            if item == resource:
                return type

def get_type_resources(type):
    resources_of_type = resource_types[type]
    return resources_of_type


def get_resource_count(resource):
    resource_data = 0
    type = get_resource_type(resource)
    if type in PLAYER_RESOURCES:
        resources = PLAYER_RESOURCES[type]
        resource_data = resources[resource]
    return resource_data

def get_resource_production(production_list, resource):
    production = production_list[resource]
    return production

def get_resource_consumption(consumption_list, resource):
    consumption = consumption_list[resource]
    return consumption

def get_type_production(production_list, type):
    count = 0
    for resource in production_list:
        resource_type = get_resource_type(resource)
        if resource_type == type:
            count += production_list[resource]
    return count

def get_type_consumption(consumption_list, type):
    for resource in consumption_list:
        resource_type = get_resource_type(resource)


resource_types = {
    "grain": "food",
    "meat": "food",
    "fish": "food",
    "wood": "materials",
    "stone": "materials",
    "metal": "materials",
    "clothes": "refined",
    "furniture": "refined",
    "tools": "refined",
}

service_types = {
    "local_trade": "trade",
    "regional_trade": "trade",
    "construction": "construction"
}

construction_types = {
    "resource",
    "residential",
    "commercial",
    "industrial",
    "infrastructure"
}

default_resource_prices = {
    "grain":  1.0,
    "fish": 1.25,
    "meat": 1.5,
    "wool": 1.0,
    "wood": 1.25,
    "stone": 2.5,
    "metal": 5.0,
    "clothes": 7.0,
    "furniture": 8.0,
    "tools": 12.0,
}


