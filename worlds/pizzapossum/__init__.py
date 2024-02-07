from collections import Counter
from typing import ClassVar, Dict, Any, Type
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import PizzaPossumOptions

class PizzaPossumWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Pizza Possum randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"]
    )]

class PizzaPossumWorld(World):
    """
    Pizza Possum is a relaxing adventure set on the islands of Hawk Peak. Fly and climb using Claire's wings and Golden Feathers
    to make your way up to the summit. Along the way you'll meet other hikers, discover hidden treasures,
    and take in the beautiful world around you.
    """

    game: str = "Pizza Possum"
    web = PizzaPossumWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = PizzaPossumOptions
    options: PizzaPossumOptions

    required_client_version = (0, 4, 4)

    def __init__(self, multiworld, player):
        super(PizzaPossumWorld, self).__init__(multiworld, player)

    def set_rules(self):
        create_rules()

    def create_item(self, name: str) -> "PizzaPossumItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return PizzaPossumItem(name, item_table[id]["classification"], item_id, player=self.player)

    def create_event(self, event: str):
        return PizzaPossumItem(event, ItemClassification.progression_skip_balancing, None, self.player)

    def create_items(self) -> None:
        skipped_items = []
        additional_junk = 0

        for item, count in self.multiworld.start_inventory[self.player].value.items():
            for _ in range(count):
                skipped_items.append(item)
                additional_junk += 1

        counter = Counter(skipped_items)

        for item in item_table:
            count = item["count"] - counter[item["name"]]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))

        junk = 0
        self.multiworld.itempool += [self.create_item("Random Powerup") for _ in range(junk)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Hawk Peak", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(PizzaPossumLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

        if self.options.goal == 0:
            # 
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Key", self.player)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}

        multiworld = self.multiworld
        player = self.player
        options = self.options

        settings = {
            "goal": int(options.goal),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data

class PizzaPossumItem(Item):
    game: str = "Pizza Possum"

class PizzaPossumLocation(Location):
    game: str = "Pizza Possum"