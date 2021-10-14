from data.player_city import PLAYER_RESOURCES


class Resource:
    type = str
    count = float
    production = float
    consumption = float

def get_resource_type(resource):
    for type in resource_types:
        resources_of_type = resource_types[type]
        for item in resources_of_type:
            if item == resource:
                return type

def get_resource_count(resource):
    type = get_resource_type(resource)
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


resource_types = {
    "food": {"grain", "meat", "fish"},
    "materials": {"wood","stone","metal"},
    "refined": {"clothes","furniture","tools","weapons"},
    "trade":{"local_trade","regional_trade"},
    "construction":{"resource","residential","commercial","industrial"}
}


