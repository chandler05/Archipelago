from typing import Dict, List, Set
from worlds.generic.Rules import forbid_item, forbid_items_for_player, set_rule, add_rule
from BaseClasses import CollectionState
from .Items import item_table


def create_rules(self, location_table):
    world = self.multiworld
    player = self.player

    mainland_packs = [pack["name"] for pack in item_table if pack["location"] == 1 and pack["name"].endswith("Booster Pack")]

    set_rule(world.get_location("Have 5 Ideas", self.player),
        lambda state: state.group_count("Mainland Ideas", player) >= 5)
    set_rule(world.get_location("Have 10 Ideas", self.player),
        lambda state: state.group_count("Mainland Ideas", player) >= 10)
    
    set_rule(world.get_location("Unlock All Packs", self.player),
        lambda state: state.has_all(set(mainland_packs), player))

    for loc in location_table:
        if "Mainland" in loc["potentialBoosterPacks"]:
            set_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_any(set(mainland_packs), player))
        elif len(loc["potentialBoosterPacks"]) > 0:
            set_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_any(set(loc["potentialBoosterPacks"]), player))
        if len(loc["ideas"]) > 0:
            set_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_all(set(loc["ideas"]), player))