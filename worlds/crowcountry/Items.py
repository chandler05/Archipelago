from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 510202400

item_table: List[ItemDict] = [
    {"name": "Small Med Kit", "id": base_id + 1, "count": 1, "classification": ItemClassification.filler},
    {"name": "Large Med Kit", "id": base_id + 2, "count": 1, "classification": ItemClassification.filler},
    {"name": "Antidote", "id": base_id + 3, "count": 2, "classification": ItemClassification.filler},
    {"name": "Grenade", "id": base_id + 4, "count": 0, "classification": ItemClassification.useful},
    {"name": "Handgun Ammo", "id": base_id + 5, "count": 3, "classification": ItemClassification.useful},
    {"name": "Shotgun Ammo", "id": base_id + 6, "count": 1, "classification": ItemClassification.useful},
    {"name": "Magnum Ammo", "id": base_id + 7, "count": 0, "classification": ItemClassification.useful},
    {"name": "Pocket Light", "id": base_id + 8, "count": 1, "classification": ItemClassification.progression},
    {"name": "Handgun Laser Sight", "id": base_id + 9, "count": 1, "classification": ItemClassification.useful},
]

group_table: Dict[str, Set[str]] = {
    "Junk": {"Small Med Kit", "Large Med Kit", "Antidote", "Handgun Ammo", "Shotgun Ammo", "Grenade"},
}