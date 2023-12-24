from collections import Counter
from typing import ClassVar, Dict, Any, Type
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import TinykinOptions

class TinykinWeb(WebWorld):
    theme = "partyTime"

class TinykinWorld(World):
    """
    Tinykin.
    """

    game: str = "Tinykin"
    web = TinykinWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc: location_table[loc].id for loc in location_table}
    location_name_to_game_id = {loc: location_table[loc].inGameId for loc in location_table}

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = TinykinOptions
    options: TinykinOptions

    required_client_version = (0, 4, 4)

    def __init__(self, multiworld, player):
        super(TinykinWorld, self).__init__(multiworld, player)

    def set_rules(self):
        create_rules()

    def create_item(self, name: str) -> "TinykinItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return TinykinItem(name, item_table[id]["classification"], item_id, player=self.player)

    def create_event(self, event: str):
        return TinykinItem(event, ItemClassification.progression_skip_balancing, None, self.player)

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

        junk = 45
        self.multiworld.itempool += [self.create_item("Nothing") for _ in range(junk)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Chrysal Workshop", self.player, self.multiworld)
        transidor_region = Region("Transidor Crossing", self.player, self.multiworld)
        sanctar_region = Region("City of Sanctar", self.player, self.multiworld)
        foliana_region = Region("Foliana Heights", self.player, self.multiworld)
        balnea_toilet_region = Region("Waters of Balnea Toilet Room", self.player, self.multiworld)
        balnea_bath_region = Region("Waters of Balnea Bathtub Room", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(TinykinLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)
        
        #self.multiworld.completion_condition[self.player] = lambda state: get_feather_state(self, 6, 8, 7, state)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        locations: Dict[int, Any] = {}

        multiworld = self.multiworld
        player = self.player
        options = self.options

        for loc in multiworld.get_filled_locations(player):
            if loc.item.code == None:
                continue
            else:
                data = {
                    "ap_id": loc.address,
                    "item_name": loc.item.name,
                    "player_name": multiworld.player_name[loc.item.player],
                    "type": int(loc.item.classification),
                }

                locations[self.location_name_to_game_id[loc.name]] = data

        settings = {
            "goal": int(options.goal),
        }
    
        slot_data = {
            "locations": locations,
            "settings": settings,
        }
    
        return slot_data

class TinykinItem(Item):
    game: str = "Tinykin"

class TinykinLocation(Location):
    game: str = "Tinykin"