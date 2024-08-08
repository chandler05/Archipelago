from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 308202200

item_table: List[ItemDict] = [
    {"name": "Bubble", "id": base_id + 1, "count": 1, "classification": ItemClassification.progression},
    {"name": "Soapboard", "id": base_id + 2, "count": 1, "classification": ItemClassification.progression},
    #{"name": "Sanctar Key", "id": base_id + 3, "count": 1, "classification": ItemClassification.progression}, Unlock door by default
    {"name": "Play Button", "id": base_id + 3, "count": 1, "classification": ItemClassification.progression},
    {"name": "Sphinx's Nose", "id": base_id + 4, "count": 1, "classification": ItemClassification.useful},
    {"name": "Mail (City of Sanctar)", "id": base_id + 5, "count": 4, "classification": ItemClassification.useful},
    {"name": "Ring (City of Sanctar)", "id": base_id + 6, "count": 1, "classification": ItemClassification.useful},
    {"name": "Screwdriver (City of Sanctar)", "id": base_id + 7, "count": 1, "classification": ItemClassification.useful},
    {"name": "Monster Photo", "id": base_id + 8, "count": 1, "classification": ItemClassification.useful},
    {"name": "Cat Door Chip", "id": base_id + 9, "count": 1, "classification": ItemClassification.progression},
    {"name": "50 Pollen (City of Sanctar)", "id": base_id + 10, "count": 5, "classification": ItemClassification.useful},
    {"name": "Artifact", "id": base_id + 11, "count": 3, "classification": ItemClassification.filler},
    {"name": "Nothing", "id": base_id + 12, "count": 0, "classification": ItemClassification.filler},
]

group_table: Dict[str, Set[str]] = {
}