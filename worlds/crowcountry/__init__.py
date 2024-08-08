from typing import ClassVar, Dict, Any, Type
from BaseClasses import Item, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import CrowCountryOptions
from .Regions import create_regions

class CrowCountryWeb(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Crow Country randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"]
    )]

class CrowCountryWorld(World):
    """
    Crow Country
    """

    game = "Crow Country"
    web = CrowCountryWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}    
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}
    location_name_to_area = {loc["name"]: loc["area"] for loc in location_table}

    object_shuffle_pairs: Dict[str, str]

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = CrowCountryOptions
    options: CrowCountryOptions

    required_client_version = (0, 4, 4)

    def create_item(self, name: str) -> "CrowCountryItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return CrowCountryItem(name, item_table[id]["classification"], item_id, player=self.player)
    
    def get_filler_item_name(self) -> str:
        return self.random.choice(list(self.item_name_groups["Junk"]))

    def create_items(self) -> None:
        for item in item_table:
            count = item["count"]
            
            if item["name"] == "Vacation Beach Gate Unlock" and self.options.starting_gate == 0:
                count = 0
                self.multiworld.push_precollected(self.create_item(item["name"]))
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))

        junk = 10
        for i in range(junk):
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options

        settings = {
            #"beachGate": int(options.beach_memory_count),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data

class CrowCountryItem(Item):
    game: str = "Crow Country"