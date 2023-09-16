from typing import List, TypedDict


class LocationInfo(TypedDict):
    name: str
    id: int
    game_id: str
    potentialBoosterPacks: List[str]
    ideas: List[str]

base_id = 91000

location_table: List[LocationInfo] = [
    {"name": "Open the Booster Pack", "id": base_id + 1, "game_id": "open_starter_pack", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Drag the Villager on top of the Berry Bush", "id": base_id + 2, "game_id": "pick_berrybush", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Mine a Rock using a Villager", "id": base_id + 3, "game_id": "punch_rock", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Sell a Card", "id": base_id + 4, "game_id": "sell_card", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Buy the Humble Beginnings Card Pack", "id": base_id + 5, "game_id": "buy_booster", "potentialBoosterPacks": ["Humble Beginnings Booster Pack"], "ideas": []},
    {"name": "Harvest a Tree using a Villager", "id": base_id + 6, "game_id": "punch_tree", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Make a Stick from Wood", "id": base_id + 7, "game_id": "carve_stick", "potentialBoosterPacks": [], "ideas": ["Idea: Stick"]},
    {"name": "Pause using the play icon in the top right corner", "id": base_id + 8, "game_id": "pause_game", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Grow a Berry Bush using Soil", "id": base_id + 9, "game_id": "plant_berry_bush", "potentialBoosterPacks": ["Humble Beginnings Booster Pack", "Reap & Sow Booster Pack"], "ideas": ["Idea: Growth"]},
    {"name": "Build a House", "id": base_id + 10, "game_id": "build_house", "potentialBoosterPacks": [], "ideas": ["Idea: House"]},
    {"name": "Get a Second Villager", "id": base_id + 11, "game_id": "second_villager", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Create Offspring", "id": base_id + 12, "game_id": "create_offspring", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Offspring", "Idea: House"]},
    {"name": "Train Militia", "id": base_id + 13, "game_id": "train_militia", "potentialBoosterPacks": [], "ideas": ["Idea: Spear"]},
    {"name": "Have 3 Houses", "id": base_id + 14, "game_id": "build_3_houses", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: House"]},
    {"name": "Kill a Rat", "id": base_id + 15, "game_id": "kill_a_rat", "potentialBoosterPacks": ["Humble Beginnings Booster Pack", "Explorers Booster Pack"], "ideas": []},
    {"name": "Explore a Forest", "id": base_id + 16, "game_id": "explore_forest", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Explore a Mountain", "id": base_id + 17, "game_id": "explore_mountain", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Open a Treasure Chest", "id": base_id + 18, "game_id": "open_treasure_chest", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Kill a Skeleton", "id": base_id + 19, "game_id": "kill_a_skeleton", "potentialBoosterPacks": ["Explorers Booster Pack", "The Armory Booster Pack"], "ideas": []},
    {"name": "Find a Graveyard", "id": base_id + 20, "game_id": "find_graveyard", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Start a Campfire", "id": base_id + 21, "game_id": "start_campfire", "potentialBoosterPacks": [], "ideas": ["Idea: Cooking Devices", "Idea: Stick"]},
    {"name": "Cook Raw Meat", "id": base_id + 22, "game_id": "cook_meat", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Cook an Omelette", "id": base_id + 23, "game_id": "cook_omelette", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack", "Explorers Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Cook a Frittata", "id": base_id + 24, "game_id": "cook_frittata", "potentialBoosterPacks": ["Curious Cuisine Booster Pack", "Explorers Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Have 5 Ideas", "id": base_id + 25, "game_id": "have_5_ideas", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 10 Ideas", "id": base_id + 26, "game_id": "have_10_ideas", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 10 Wood", "id": base_id + 27, "game_id": "have_10_wood", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 10 Stone", "id": base_id + 28, "game_id": "have_10_stone", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Get a Dog", "id": base_id + 29, "game_id": "get_a_dog", "potentialBoosterPacks": ["The Armory Booster Pack", "Explorers Booster Pack"], "ideas": []},
    {"name": "Get an Iron Bar", "id": base_id + 30, "game_id": "get_iron_bar", "potentialBoosterPacks": ["Explorers Booster Pack", "Logic and Reason Booster Pack", "Order and Structure Booster Pack"], "ideas": ["Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine", "Idea: Brick", "Idea: Plank"]},
    {"name": "Train an Explorer", "id": base_id + 31, "game_id": "train_explorer", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Build a Shed", "id": base_id + 32, "game_id": "create_shed", "potentialBoosterPacks": [], "ideas": ["Idea: Shed", "Idea: Stick"]},
    {"name": "Build a Quarry", "id": base_id + 33, "game_id": "create_quarry", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Quarry"]},
    {"name": "Build a Lumber Camp", "id": base_id + 34, "game_id": "create_lumbercamp", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Lumber Camp"]},
    {"name": "Build a Farm", "id": base_id + 35, "game_id": "build_farm", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Farm", "Idea: Brick", "Idea: Plank"]},
    {"name": "Build a Brickyard", "id": base_id + 36, "game_id": "create_brickyard", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Brickyard", "Idea: Brick", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine", "Idea: Brick", "Idea: Plank"]},
    {"name": "Sell a Card at a Market", "id": base_id + 37, "game_id": "sell_at_market", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Market", "Idea: Brick", "Idea: Plank"]},
    {"name": "Buy something from a Travelling Cart", "id": base_id + 38, "game_id": "buy_from_travelling_cart", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 5 Food", "id": base_id + 39, "game_id": "have_5_food", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": []},
    {"name": "Have 10 Food", "id": base_id + 40, "game_id": "have_10_food", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": []},
    {"name": "Have 20 Food", "id": base_id + 41, "game_id": "have_20_food", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Growth"]},
    {"name": "Have 50 Food", "id": base_id + 42, "game_id": "have_50_food", "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Growth", "Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Reach Moon 6", "id": base_id + 43, "game_id": "reach_month_6", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Reach Moon 12", "id": base_id + 44, "game_id": "reach_month_12", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Reach Moon 24", "id": base_id + 45, "game_id": "reach_month_24", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Reach Moon 36", "id": base_id + 46, "game_id": "reach_month_36", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Unlock All Packs", "id": base_id + 47, "game_id": "unlock_all_packs", "potentialBoosterPacks": [], "ideas": []},
    {"name": "Get 3 Villagers", "id": base_id + 48, "game_id": "3_villagers", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Offspring", "Idea: House"]},
    {"name": "Find the Catacombs", "id": base_id + 49, "game_id": "find_catacombs", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Find a mysterious artifact", "id": base_id + 50, "game_id": "find_artifact", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Build a Temple", "id": base_id + 51, "game_id": "build_temple", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Bring the Goblet to the Temple", "id": base_id + 52, "game_id": "bring_goblet", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Kill the Demon", "id": base_id + 53, "game_id": "kill_demon", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Have 10 Gold", "id": base_id + 54, "game_id": "have_10_gold", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 30 Gold", "id": base_id + 55, "game_id": "have_30_gold", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have 50 Gold", "id": base_id + 56, "game_id": "have_50_gold", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Make a Villager wear a Rabbit Hat", "id": base_id + 57, "game_id": "wear_bunny_hat", "potentialBoosterPacks": ["Mainland"], "ideas": []},
    {"name": "Have a Villager with Combat Level 20", "id": base_id + 58, "game_id": "villager_combat_20", "potentialBoosterPacks": ["The Armory Booster Pack"], "ideas": []},
    {"name": "Train a Ninja", "id": base_id + 59, "game_id": "train_ninja", "potentialBoosterPacks": ["The Armory Booster Pack"], "ideas": ["Idea: Smithy", "Idea: Throwing Star", "Idea: Iron Bar", "Idea: Brick"]},
    {"name": "Build a Smithy", "id": base_id + 60, "game_id": "build_smithy", "potentialBoosterPacks": ["Mainland"], "ideas": ["Idea: Smithy", "Idea: Iron Bar", "Idea: Brick"]},
    {"name": "Train a Wizard", "id": base_id + 61, "game_id": "train_wizard", "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Wizard Staff"]},
]

island_quest_table: List[LocationInfo] = [

]