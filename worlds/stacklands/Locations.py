from typing import List, TypedDict


class LocationInfo(TypedDict):
    name: str
    id: int
    game_id: str
    potentialBoosterPacks: List[str]

base_id = 91000

location_table: List[LocationInfo] = [
    {"name": "Open the Booster Pack", "id": base_id + 1, "game_id": "open_starter_pack", "potentialBoosterPacks": []},
    {"name": "Drag the Villager on top of the Berry Bush", "id": base_id + 2, "game_id": "pick_berrybush", "potentialBoosterPacks": []},
    {"name": "Mine a Rock using a Villager", "id": base_id + 3, "game_id": "punch_rock", "potentialBoosterPacks": []},
    {"name": "Sell a Card", "id": base_id + 4, "game_id": "sell_card", "potentialBoosterPacks": []},
    {"name": "Buy the Humble Beginnings Card Pack", "id": base_id + 5, "game_id": "buy_booster", "potentialBoosterPacks": ["Humble Beginnings Booster Pack"]},
    {"name": "Harvest a Tree using a Villager", "id": base_id + 6, "game_id": "punch_tree", "potentialBoosterPacks": []},
    {"name": "Make a Stick from Wood", "id": base_id + 7, "game_id": "carve_stick", "potentialBoosterPacks": []},
    {"name": "Pause using the play icon in the top right corner", "id": base_id + 8, "game_id": "pause_game", "potentialBoosterPacks": []},
    {"name": "Grow a Berry Bush using Soil", "id": base_id + 9, "game_id": "plant_berry_bush", "potentialBoosterPacks": ["Humble Beginnings Booster Pack", "Reap & Sow Booster Pack"]},
    {"name": "Build a House", "id": base_id + 10, "game_id": "build_house", "potentialBoosterPacks": []},
    {"name": "Get a Second Villager", "id": base_id + 11, "game_id": "second_villager", "potentialBoosterPacks": ["Mainland"]},
    {"name": "Create Offspring", "id": base_id + 12, "game_id": "create_offspring", "potentialBoosterPacks": ["Mainland"]},
]

island_quest_table: List[LocationInfo] = [

]