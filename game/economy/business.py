from dataclasses import dataclass
from data.resource_data import RESOURCES

@datacklass
class Business:
    type: str
    worker_type: str
    demands: dict
    demand_met: list
    produces: Resource
    workers: int
    produced: list
    sold: float





