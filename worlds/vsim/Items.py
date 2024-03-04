from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 94201900

item_table: List[ItemDict] = [
    {"name": "Memory (Vacation Beach)", "id": base_id + 1, "count": 22, "classification": ItemClassification.progression},
    {"name": "Memory (Vacation Forest)", "id": base_id + 2, "count": 23, "classification": ItemClassification.progression},
    {"name": "Memory (Vacation Mountain)", "id": base_id + 3, "count": 24, "classification": ItemClassification.progression},
    {"name": "Vacation Beach Gate Unlock", "id": base_id + 4, "count": 1, "classification": ItemClassification.progression},
    {"name": "Vacation Forest Gate Unlock", "id": base_id + 5, "count": 1, "classification": ItemClassification.progression},
    {"name": "Vacation Mountain Gate Unlock", "id": base_id + 6, "count": 1, "classification": ItemClassification.progression},
    {"name": "Camera", "id": base_id + 7, "count": 1, "classification": ItemClassification.progression}
]

group_table: Dict[str, Set[str]] = {
    "Gates": {"Vacation Beach Gate Unlock",  "Vacation Forest Gate Unlock", "Vacation Mountain Gate Unlock"},
    "Memories": {"Memory (Vacation Beach)", "Memory (Vacation Forest)", "Memory (Vacation Mountain)"}
}