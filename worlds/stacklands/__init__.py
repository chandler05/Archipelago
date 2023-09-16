from typing import Dict, Any
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
#from .Options import stacklands_options

class StacklandsWeb(WebWorld):
    theme = "jungle"

class StacklandsWorld(World):
    """
    Stacklands.
    """

    game: str = "Stacklands"
    web = StacklandsWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}

    item_name_groups = group_table
    #option_definitions = stacklands_options

    required_client_version = (0, 1, 9)

    def __init__(self, multiworld, player):
        super(StacklandsWorld, self).__init__(multiworld, player)

    def set_rules(self):
        create_rules()

    def create_item(self, name: str) -> "StacklandsItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return StacklandsItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return StacklandsItem(event, ItemClassification.progression_skip_balancing, None, self.player)

    def create_items(self):
        for item in item_table:
            count = item["count"]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))
 
        junk = 0
        self.multiworld.itempool += [self.create_item("Berry Bush") for _ in range(junk)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Mainland", self.player, self.multiworld)

        #island_region = Region("Island", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(StacklandsLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def set_rules(self):
        print("Skipping set_rules")
        #create_rules(self, location_table)

class StacklandsItem(Item):
    game: str = "Stacklands"


class StacklandsLocation(Location):
    game: str = "Stacklands"