from typing import Dict, List, Set
from worlds.generic.Rules import forbid_item, forbid_items_for_player, set_rule, add_rule
from BaseClasses import CollectionState
from .Items import booster_packs_table


def create_rules(self, location_table):
    world = self.multiworld
    player = self.player

    mainland_packs = [pack["name"] for pack in booster_packs_table if pack["location"] == 1]

    for loc in location_table:
        if "Mainland" in loc["potentialBoosterPacks"]:
            set_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_any(set(mainland_packs), player))
        else:
            set_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_any(set(loc["potentialBoosterPacks"]), player))