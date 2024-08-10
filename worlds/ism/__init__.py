from collections import Counter
from typing import ClassVar, Dict, Any, Type
from BaseClasses import Region, Location, Item, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import InSoundMindOptions
from .Regions import create_regions

class InSoundMindWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the In Sound Mind randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"]
    )]

class InSoundMindWorld(World):
    """
    In Sound Mind.
    """

    game = "In Sound Mind"
    web = InSoundMindWeb()
    data_version = 2

    item_name_to_id = {item: item_table[item].id for item in item_table}
    location_name_to_id = {loc: location_table[loc].id for loc in location_table}
    location_name_to_game_id = {loc: location_table[loc].inGameId for loc in location_table}

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = InSoundMindOptions
    options: InSoundMindOptions

    required_client_version = (0, 4, 4)

    def get_filler_item_name(self) -> str:
        return "IDK"

    def create_item(self, name: str) -> "InSoundMindItem":
        item_id: int = self.item_name_to_id[name]

        return InSoundMindItem(name, item_table[name].classification, item_id, player=self.player)

    def create_items(self) -> None:
        for item in item_table:
            count = item_table[item].count
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item))

        junk = 0

    def create_regions(self) -> None:
        create_regions(self)

        #self.multiworld.completion_condition[self.player] = lambda state: state.has("Golden Feather", self.player, 12)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options

        settings = {
            "goal": int(options.goal),
            "logicLevel": int(options.golden_feather_progression),
            "costMultiplier": int(options.cost_multiplier),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data

class InSoundMindItem(Item):
    game: str = "In Sound Mind"
