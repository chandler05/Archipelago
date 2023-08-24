from enum import IntEnum
from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemLoc(IntEnum):
    none = 0
    mainland = 1
    island = 2

class ItemDict(TypedDict):
    name: str
    game_id: str
    location: ItemLoc
    count: int
    id: int
    classification: ItemClassification

base_id = 92000

booster_packs_table: List[ItemDict] = [
    # Mainland Booster Packs
    {"name": "Humble Beginnings Booster Pack", "game_id": "booster_pack_1", "location": 1, "count": 1, "id": base_id + 1, "classification": ItemClassification.progression},
    {"name": "Seeking Wisdom Booster Pack", "game_id": "booster_pack_2", "location": 1, "count": 1, "id": base_id + 2, "classification": ItemClassification.progression},
    {"name": "Reap & Sow Booster Pack", "game_id": "booster_pack_3", "location": 1, "count": 1, "id": base_id + 3, "classification": ItemClassification.progression},
    {"name": "Curious Cuisine Booster Pack", "game_id": "booster_pack_4", "location": 1, "count": 1, "id": base_id + 4, "classification": ItemClassification.progression},
    {"name": "Logic and Reason Booster Pack", "game_id": "booster_pack_5", "location": 1, "count": 1, "id": base_id + 5, "classification": ItemClassification.progression},
    {"name": "The Armory Booster Pack", "game_id": "booster_pack_6", "location": 1, "count": 1, "id": base_id + 6, "classification": ItemClassification.progression},
    {"name": "Explorers Booster Pack", "game_id": "booster_pack_7", "location": 1, "count": 1, "id": base_id + 7, "classification": ItemClassification.progression},
    {"name": "Order and Structure Booster Pack", "game_id": "booster_pack_8", "location": 1, "count": 1, "id": base_id + 8, "classification": ItemClassification.progression},

    # Island Booster Packs
    {"name": "On The Shore Booster Pack", "game_id": "island_booster_pack_1", "location": 2, "count": 1, "id": base_id + 9, "classification": ItemClassification.progression},
    {"name": "Island of Ideas Booster Pack", "game_id": "island_booster_pack_2", "location": 2, "count": 1, "id": base_id + 10, "classification": ItemClassification.progression},
    {"name": "Grilling and Brewing Booster Pack", "game_id": "island_booster_pack_3", "location": 2, "count": 1, "id": base_id + 11, "classification": ItemClassification.progression},
    {"name": "Island Insights Booster Pack", "game_id": "island_booster_pack_4", "location": 2, "count": 1, "id": base_id + 12, "classification": ItemClassification.progression},
    {"name": "Advanced Archipelago Booster Pack", "game_id": "island_booster_pack_5", "location": 2, "count": 1, "id": base_id + 13, "classification": ItemClassification.progression},
    {"name": "Enclave Explorers Booster Pack", "game_id": "island_booster_pack_6", "location": 2, "count": 1, "id": base_id + 14, "classification": ItemClassification.progression},
]

filler_cards_table: List[ItemDict] = [
    
]

group_table: Dict[str, Set[str]] = {

}