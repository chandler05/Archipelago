from typing import Dict, Any
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import stacklands_options

class StacklandsWeb(WebWorld):
    theme = "ocean"

class ShortHikeWorld(World):
    """
    A Short Hike is a relaxing adventure set on the islands of Hawk Peak. Fly and climb using Claire's wings and Golden Feathers
    to make your way up to the summit. Along the way you'll meet other hikers, discover hidden treasures,
    and take in the beautiful world around you.
    """

    game: str = "Stacklands"
    web = StacklandsWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}
    location_name_to_game_id = {loc["name"]: loc["inGameId"] for loc in location_table}
    location_name_to_chest_angle = {loc["name"]: loc["chestAngle"] for loc in location_table}

    item_name_groups = group_table
    option_definitions = stacklands_options

    required_client_version = (0, 1, 9)

    def __init__(self, multiworld, player):
        super(ShortHikeWorld, self).__init__(multiworld, player)

    def set_rules(self):
        create_rules()

    def create_item(self, name: str) -> "StacklandsItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return StacklandsItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return StacklandsItem(event, ItemClassification.progression_skip_balancing, None, self.player)

    def create_items(self) -> None:
        for item in item_table:
            count = item["count"]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))
 
        junk = 21 - self.multiworld.filler_silver_feathers[self.player].value
        self.multiworld.itempool += [self.create_item("13 Coins") for _ in range(junk)]
        self.multiworld.itempool += [self.create_item("Silver Feather") for _ in range(self.multiworld.filler_silver_feathers[self.player].value)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Mainland", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(StacklandsLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        locations: Dict[int, Any] = {}

        world = self.multiworld
        player = self.player

        for loc in world.get_filled_locations(player):
            if loc.item.code == None:
                continue
            else:
                data = {
                    "ap_id": loc.address,
                    "item_name": loc.item.name,
                    "player_name": world.player_name[loc.item.player],
                    "type": int(loc.item.classification),
                    "chest_angle": self.location_name_to_chest_angle[loc.name],
                }

                locations[self.location_name_to_game_id[loc.name]] = data

        settings = {
            "goal": world.goal[player].value,
            "showGoldenChests": bool(world.show_golden_chests[player].value),
            "skipCutscenes": bool(world.skip_cutscenes[player].value),
        }
    
        slot_data = {
            "locations": locations,
            "settings": settings,
        }
    
        return slot_data


class StacklandsItem(Item):
    game: str = "Stacklands"


class StacklandsLocation(Location):
    game: str = "Stacklands"