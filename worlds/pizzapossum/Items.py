from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 20231000

item_table: List[ItemDict] = [
    {"name": "Key", "id": base_id + 1, "count": 15, "classification": ItemClassification.progression},
]

group_table: Dict[str, Set[str]] = {
}