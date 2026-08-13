from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world
from . import options as zaw_options
from .names import Game

class ZackAndWikiWorld(World):
    """
    Zack & Wiki: Quest for Barbaros' Treasure is a 2007 point-and-click Wii puzzle game.
    Set out on an adventure in search of Treasure Island and become legendary pirates!
    """

    game = Game.GAME

    web = web_world.ZackAndWikiWebWorld()

    options_dataclass = zaw_options.ZackAndWikiOptions
    options: zaw_options.ZackAndWikiOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.ZackAndWikiItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    #def fill_slot_data(self) -> Mapping[str, Any]:
        #return self.options.as_dict(
            #"hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
        #)
