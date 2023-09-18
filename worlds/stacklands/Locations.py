from typing import List, TypedDict


class LocationInfo(TypedDict):
    name: str
    id: int
    game_id: str
    requireBasicPacks: bool
    potentialBoosterPacks: List[str]
    ideas: List[str]

base_id = 91000

location_table: List[LocationInfo] = [
    # Mainland Quests
    {"name": "Open the Booster Pack", "id": base_id + 1, "game_id": "open_starter_pack", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Drag the Villager on top of the Berry Bush", "id": base_id + 2, "game_id": "pick_berrybush", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Mine a Rock using a Villager", "id": base_id + 3, "game_id": "punch_rock", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Sell a Card", "id": base_id + 4, "game_id": "sell_card", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Buy the Humble Beginnings Pack", "id": base_id + 5, "game_id": "buy_booster", "requireBasicPacks": True, "potentialBoosterPacks": ["Humble Beginnings Booster Pack"], "ideas": []},
    {"name": "Harvest a Tree using a Villager", "id": base_id + 6, "game_id": "punch_tree", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Make a Stick from Wood", "id": base_id + 7, "game_id": "carve_stick", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": ["Idea: Stick"]},
    {"name": "Pause using the play icon in the top right corner", "id": base_id + 8, "game_id": "pause_game", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Grow a Berry Bush using Soil", "id": base_id + 9, "game_id": "plant_berry_bush", "requireBasicPacks": False, "potentialBoosterPacks": ["Humble Beginnings Booster Pack", "Reap & Sow Booster Pack"], "ideas": ["Idea: Growth"]},
    {"name": "Build a House", "id": base_id + 10, "game_id": "build_house", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: House"]},
    {"name": "Get a Second Villager", "id": base_id + 11, "game_id": "second_villager", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Create Offspring", "id": base_id + 12, "game_id": "create_offspring", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Offspring", "Idea: House"]},
    {"name": "Train Militia", "id": base_id + 13, "game_id": "train_militia", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Spear"]},
    {"name": "Have 3 Houses", "id": base_id + 14, "game_id": "build_3_houses", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: House"]},
    {"name": "Kill a Rat", "id": base_id + 15, "game_id": "kill_a_rat", "requireBasicPacks": True, "potentialBoosterPacks": ["Humble Beginnings Booster Pack", "Explorers Booster Pack"], "ideas": []},
    {"name": "Explore a Forest", "id": base_id + 16, "game_id": "explore_forest", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Explore a Mountain", "id": base_id + 17, "game_id": "explore_mountain", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Open a Treasure Chest", "id": base_id + 18, "game_id": "open_treasure_chest", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Kill a Skeleton", "id": base_id + 19, "game_id": "kill_a_skeleton", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack", "The Armory Booster Pack"], "ideas": []},
    {"name": "Find a Graveyard", "id": base_id + 20, "game_id": "find_graveyard", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Start a Campfire", "id": base_id + 21, "game_id": "start_campfire", "requireBasicPacks": False, "potentialBoosterPacks": [], "ideas": ["Idea: Cooking Devices", "Idea: Stick"]},
    {"name": "Cook Raw Meat", "id": base_id + 22, "game_id": "cook_meat", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Cook an Omelette", "id": base_id + 23, "game_id": "cook_omelette", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack", "Explorers Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Cook a Frittata", "id": base_id + 24, "game_id": "cook_frittata", "requireBasicPacks": True, "potentialBoosterPacks": ["Curious Cuisine Booster Pack", "Explorers Booster Pack"], "ideas": ["Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Have 5 Ideas", "id": base_id + 25, "game_id": "have_5_ideas", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have 10 Ideas", "id": base_id + 26, "game_id": "have_10_ideas", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have 10 Wood", "id": base_id + 27, "game_id": "have_10_wood", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have 10 Stone", "id": base_id + 28, "game_id": "have_10_stone", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Get a Dog", "id": base_id + 29, "game_id": "get_a_dog", "requireBasicPacks": True, "potentialBoosterPacks": ["The Armory Booster Pack", "Explorers Booster Pack"], "ideas": []},
    {"name": "Get an Iron Bar", "id": base_id + 30, "game_id": "get_iron_bar", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack", "Logic and Reason Booster Pack", "Order and Structure Booster Pack"], "ideas": ["Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine", "Idea: Brick", "Idea: Plank"]},
    {"name": "Train an Explorer", "id": base_id + 31, "game_id": "train_explorer", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Build a Shed", "id": base_id + 32, "game_id": "create_shed", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Shed", "Idea: Stick"]},
    {"name": "Build a Quarry", "id": base_id + 33, "game_id": "create_quarry", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Quarry"]},
    {"name": "Build a Lumber Camp", "id": base_id + 34, "game_id": "create_lumbercamp", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Lumber Camp"]},
    {"name": "Build a Farm", "id": base_id + 35, "game_id": "build_farm", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Farm", "Idea: Brick", "Idea: Plank"]},
    {"name": "Build a Brickyard", "id": base_id + 36, "game_id": "create_brickyard", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Brickyard", "Idea: Brick", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine", "Idea: Brick", "Idea: Plank"]},
    {"name": "Sell a Card at a Market", "id": base_id + 37, "game_id": "sell_at_market", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Market", "Idea: Brick", "Idea: Plank"]},
    {"name": "Buy something from a Travelling Cart", "id": base_id + 38, "game_id": "buy_from_travelling_cart", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have 5 Food", "id": base_id + 39, "game_id": "have_5_food", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": []},
    {"name": "Have 10 Food", "id": base_id + 40, "game_id": "have_10_food", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": []},
    {"name": "Have 20 Food", "id": base_id + 41, "game_id": "have_20_food", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Growth"]},
    {"name": "Have 50 Food", "id": base_id + 42, "game_id": "have_50_food", "requireBasicPacks": True, "potentialBoosterPacks": ["Reap & Sow Booster Pack", "Curious Cuisine Booster Pack"], "ideas": ["Idea: Growth", "Idea: Cooking Devices", "Idea: Foodstuffs"]},
    {"name": "Reach Moon 6", "id": base_id + 43, "game_id": "reach_month_6", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Reach Moon 12", "id": base_id + 44, "game_id": "reach_month_12", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Reach Moon 24", "id": base_id + 45, "game_id": "reach_month_24", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Reach Moon 36", "id": base_id + 46, "game_id": "reach_month_36", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Stick, Idea: Brick, Idea: Plank"]},
    {"name": "Unlock All Packs", "id": base_id + 47, "game_id": "unlock_all_packs", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Get 3 Villagers", "id": base_id + 48, "game_id": "3_villagers", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Offspring", "Idea: House"]},
    {"name": "Find the Catacombs", "id": base_id + 49, "game_id": "find_catacombs", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Find a mysterious artifact", "id": base_id + 50, "game_id": "find_artifact", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": []},
    {"name": "Build a Temple", "id": base_id + 51, "game_id": "build_temple", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Bring the Goblet to the Temple", "id": base_id + 52, "game_id": "bring_goblet", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Kill the Demon", "id": base_id + 53, "game_id": "kill_demon", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Temple", "Idea: Brick", "Idea: Plank", "Idea: Iron Bar", "Idea: Smelter", "Idea: Iron Mine"]},
    {"name": "Have 10 Coins", "id": base_id + 54, "game_id": "have_10_gold", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have 30 Coins", "id": base_id + 55, "game_id": "have_30_gold", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Market"]},
    {"name": "Have 50 Coins", "id": base_id + 56, "game_id": "have_50_gold", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Market"]},
    {"name": "Make a Villager wear a Rabbit Hat", "id": base_id + 57, "game_id": "wear_bunny_hat", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": []},
    {"name": "Have a Villager with Combat Level 20", "id": base_id + 58, "game_id": "villager_combat_20", "requireBasicPacks": True, "potentialBoosterPacks": ["The Armory Booster Pack"], "ideas": []},
    {"name": "Train a Ninja", "id": base_id + 59, "game_id": "train_ninja", "requireBasicPacks": True, "potentialBoosterPacks": ["The Armory Booster Pack"], "ideas": ["Idea: Smithy", "Idea: Throwing Star", "Idea: Iron Bar", "Idea: Brick"]},
    {"name": "Build a Smithy", "id": base_id + 60, "game_id": "build_smithy", "requireBasicPacks": True, "potentialBoosterPacks": [], "ideas": ["Idea: Smithy", "Idea: Iron Bar", "Idea: Brick"]},
    {"name": "Train a Wizard", "id": base_id + 61, "game_id": "train_wizard", "requireBasicPacks": True, "potentialBoosterPacks": ["Explorers Booster Pack"], "ideas": ["Idea: Wizard Staff"]},
]