from enum import IntEnum
from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemLoc(IntEnum):
    none = 0
    mainland = 1
    island = 2

class ItemDict(TypedDict):
    name: str
    location: ItemLoc
    count: int
    id: int
    classification: ItemClassification

base_id = 92000

item_table: List[ItemDict] = [
    # Mainland Booster Packs
    {"name": "Humble Beginnings Booster Pack", "location": 1, "count": 1, "id": base_id + 1, "classification": ItemClassification.progression},
    {"name": "Seeking Wisdom Booster Pack", "location": 1, "count": 1, "id": base_id + 2, "classification": ItemClassification.progression},
    {"name": "Reap & Sow Booster Pack", "location": 1, "count": 1, "id": base_id + 3, "classification": ItemClassification.progression},
    {"name": "Curious Cuisine Booster Pack", "location": 1, "count": 1, "id": base_id + 4, "classification": ItemClassification.progression},
    {"name": "Logic and Reason Booster Pack", "location": 1, "count": 1, "id": base_id + 5, "classification": ItemClassification.progression_skip_balancing},
    {"name": "The Armory Booster Pack", "location": 1, "count": 1, "id": base_id + 6, "classification": ItemClassification.progression_skip_balancing},
    {"name": "Explorers Booster Pack", "location": 1, "count": 1, "id": base_id + 7, "classification": ItemClassification.progression_skip_balancing},
    {"name": "Order and Structure Booster Pack", "location": 1, "count": 1, "id": base_id + 8, "classification": ItemClassification.progression_skip_balancing},

    # Mainland Ideas
    {"name": "Idea: Animal Pen", "location": 1, "count": 1, "id": base_id + 9, "classification": ItemClassification.filler},
    {"name": "Idea: Axe", "location": 1, "count": 1, "id": base_id + 10, "classification": ItemClassification.filler},
    {"name": "Idea: Bone Spear", "location": 1, "count": 1, "id": base_id + 11, "classification": ItemClassification.filler},
    {"name": "Idea: Boomerang", "location": 1, "count": 1, "id": base_id + 12, "classification": ItemClassification.filler},
    {"name": "Idea: Breeding Pen", "location": 1, "count": 1, "id": base_id + 13, "classification": ItemClassification.filler},
    {"name": "Idea: Brick", "location": 1, "count": 1, "id": base_id + 14, "classification": ItemClassification.progression},
    {"name": "Idea: Brickyard", "location": 1, "count": 1, "id": base_id + 15, "classification": ItemClassification.progression},
    {"name": "Idea: Butchery", "location": 1, "count": 1, "id": base_id + 16, "classification": ItemClassification.filler},
    {"name": "Idea: Chainmail Armor", "location": 1, "count": 1, "id": base_id + 17, "classification": ItemClassification.filler},
    {"name": "Idea: Chicken", "location": 1, "count": 1, "id": base_id + 18, "classification": ItemClassification.filler},
    {"name": "Idea: Club", "location": 1, "count": 1, "id": base_id + 19, "classification": ItemClassification.filler},
    {"name": "Idea: Coin Chest", "location": 1, "count": 1, "id": base_id + 20, "classification": ItemClassification.filler},
    {"name": "Idea: Crane", "location": 1, "count": 1, "id": base_id + 21, "classification": ItemClassification.filler},
    {"name": "Idea: Dustbin", "location": 1, "count": 1, "id": base_id + 22, "classification": ItemClassification.filler},
    {"name": "Idea: Farm", "location": 1, "count": 1, "id": base_id + 23, "classification": ItemClassification.filler},
    {"name": "Idea: Garden", "location": 1, "count": 1, "id": base_id + 24, "classification": ItemClassification.filler},
    {"name": "Idea: Growth", "location": 1, "count": 1, "id": base_id + 25, "classification": ItemClassification.progression},
    {"name": "Idea: Hammer", "location": 1, "count": 1, "id": base_id + 26, "classification": ItemClassification.filler},
    {"name": "Idea: House", "location": 1, "count": 1, "id": base_id + 27, "classification": ItemClassification.progression},
    {"name": "Idea: Iron Bar", "location": 1, "count": 1, "id": base_id + 28, "classification": ItemClassification.progression},
    {"name": "Idea: Iron Mine", "location": 1, "count": 1, "id": base_id + 29, "classification": ItemClassification.progression},
    {"name": "Idea: Iron Shield", "location": 1, "count": 1, "id": base_id + 30, "classification": ItemClassification.filler},
    {"name": "Idea: Lumber Camp", "location": 1, "count": 1, "id": base_id + 31, "classification": ItemClassification.progression},
    {"name": "Idea: Magic Blade", "location": 1, "count": 1, "id": base_id + 32, "classification": ItemClassification.filler},
    {"name": "Idea: Magic Glue", "location": 1, "count": 1, "id": base_id + 33, "classification": ItemClassification.filler},
    {"name": "Idea: Magic Ring", "location": 1, "count": 1, "id": base_id + 34, "classification": ItemClassification.filler},
    {"name": "Idea: Magic Staff", "location": 1, "count": 1, "id": base_id + 35, "classification": ItemClassification.progression},
    {"name": "Idea: Magic Tome", "location": 1, "count": 1, "id": base_id + 36, "classification": ItemClassification.filler},
    {"name": "Idea: Magic Wand", "location": 1, "count": 1, "id": base_id + 37, "classification": ItemClassification.filler},
    {"name": "Idea: Market", "location": 1, "count": 1, "id": base_id + 38, "classification": ItemClassification.progression},
    {"name": "Idea: Offspring", "location": 1, "count": 1, "id": base_id + 39, "classification": ItemClassification.progression},
    {"name": "Idea: Pickaxe", "location": 1, "count": 1, "id": base_id + 40, "classification": ItemClassification.filler},
    {"name": "Idea: Plank", "location": 1, "count": 1, "id": base_id + 41, "classification": ItemClassification.progression},
    {"name": "Idea: Quarry", "location": 1, "count": 1, "id": base_id + 42, "classification": ItemClassification.progression},
    {"name": "Idea: Resource Chest", "location": 1, "count": 1, "id": base_id + 43, "classification": ItemClassification.filler},
    {"name": "Idea: Resource Magnet", "location": 1, "count": 1, "id": base_id + 44, "classification": ItemClassification.filler},
    {"name": "Idea: Sawmill", "location": 1, "count": 1, "id": base_id + 45, "classification": ItemClassification.progression},
    {"name": "Idea: Shed", "location": 1, "count": 1, "id": base_id + 46, "classification": ItemClassification.filler},
    {"name": "Idea: Slingshot", "location": 1, "count": 1, "id": base_id + 47, "classification": ItemClassification.filler},
    {"name": "Idea: Smithy", "location": 1, "count": 1, "id": base_id + 48, "classification": ItemClassification.progression},
    {"name": "Idea: Smelter", "location": 1, "count": 1, "id": base_id + 49, "classification": ItemClassification.progression},
    {"name": "Idea: Spear", "location": 1, "count": 1, "id": base_id + 50, "classification": ItemClassification.useful},
    {"name": "Idea: Spiked Plank", "location": 1, "count": 1, "id": base_id + 51, "classification": ItemClassification.filler},
    {"name": "Idea: Stick", "location": 1, "count": 1, "id": base_id + 52, "classification": ItemClassification.progression},
    {"name": "Idea: Sword", "location": 1, "count": 1, "id": base_id + 53, "classification": ItemClassification.useful},
    {"name": "Idea: Temple", "location": 1, "count": 1, "id": base_id + 54, "classification": ItemClassification.progression},
    {"name": "Idea: Throwing Stars", "location": 1, "count": 1, "id": base_id + 55, "classification": ItemClassification.progression},
    {"name": "Idea: University", "location": 1, "count": 1, "id": base_id + 56, "classification": ItemClassification.filler},
    {"name": "Idea: Warehouse", "location": 1, "count": 1, "id": base_id + 57, "classification": ItemClassification.filler},
    {"name": "Idea: Wizard Robe", "location": 1, "count": 1, "id": base_id + 58, "classification": ItemClassification.filler},
    {"name": "Idea: Wooden Shield", "location": 1, "count": 1, "id": base_id + 59, "classification": ItemClassification.filler},
    {"name": "Idea: Foodstuffs", "location": 1, "count": 1, "id": base_id + 60, "classification": ItemClassification.progression},
    {"name": "Idea: Cooking Devices", "location": 1, "count": 1, "id": base_id + 61, "classification": ItemClassification.progression},

    # Island Booster Packs
    #{"name": "On The Shore Booster Pack", "location": 2, "count": 1, "id": base_id + 9, "classification": ItemClassification.progression},
    #{"name": "Island of Ideas Booster Pack", "location": 2, "count": 1, "id": base_id + 10, "classification": ItemClassification.progression},
    #{"name": "Grilling and Brewing Booster Pack", "location": 2, "count": 1, "id": base_id + 11, "classification": ItemClassification.progression},
    #{"name": "Island Insights Booster Pack", "location": 2, "count": 1, "id": base_id + 12, "classification": ItemClassification.progression},
    #{"name": "Advanced Archipelago Booster Pack", "location": 2, "count": 1, "id": base_id + 13, "classification": ItemClassification.progression},
    #{"name": "Enclave Explorers Booster Pack", "location": 2, "count": 1, "id": base_id + 14, "classification": ItemClassification.progression},
]

group_table: Dict[str, Set[str]] = {
    "Basic Mainland Booster Packs": {"Humble Beginnings Booster Pack", "Seeking Wisdom Booster Pack"},
    "Mainland Booster Packs": {"Humble Beginnings Booster Pack", "Seeking Wisdom Booster Pack", "Reap & Sow Booster Pack", "Curious Cuisine Booster Pack", "Logic and Reason Booster Pack", "The Armory Booster Pack", "Explorers Booster Pack", "Order and Structure Booster Pack"},
    "Mainland Ideas": set(idea["name"] for idea in item_table if idea["location"] == 1 and idea["name"].startswith("Idea:")),
    "Obtainable": {"Idea: Stick"},
}