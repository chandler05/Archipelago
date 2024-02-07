from typing import List, TypedDict

class LocationInfo(TypedDict):
    name: str
    id: int

base_id = 20232000

location_table: List[LocationInfo] = [
    {"name": "Key Unlock 1", "id": base_id + 1},
    {"name": "Key Unlock 2", "id": base_id + 2},
    {"name": "Key Unlock 3", "id": base_id + 3},
    {"name": "Key Unlock 4", "id": base_id + 4},
    {"name": "Key Unlock 5", "id": base_id + 5},
    {"name": "Key Unlock 6", "id": base_id + 6},
    {"name": "Key Unlock 7", "id": base_id + 7},
    {"name": "Key Unlock 8", "id": base_id + 8},
    {"name": "Key Unlock 9", "id": base_id + 9},
    {"name": "Key Unlock 10", "id": base_id + 10},
    {"name": "Key Unlock 11", "id": base_id + 11},
    {"name": "Key Unlock 12", "id": base_id + 12},
    {"name": "Key Unlock 13", "id": base_id + 13},
    {"name": "Key Unlock 14", "id": base_id + 14},
    {"name": "Key Unlock 15", "id": base_id + 15},
]
