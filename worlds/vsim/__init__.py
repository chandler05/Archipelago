from typing import ClassVar, Dict, Any, Type
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table, base_id
from .Locations import location_table
from .Rules import create_rules
from .Options import VacationSimOptions

class VacationSimWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Vacation Simulator randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"]
    )]

class VacationSimWorld(World):
    """
    Visit the vibrant world of Vacation Island and make real memories of a simulated vacation!
    Explore activity-rich destinations filled with a colorful cast of Bots and endless interactions to approximate recreation.
    """

    game = "Vacation Simulator"
    web = VacationSimWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}
    location_name_to_game_id = {loc["name"]: loc["inGameId"] for loc in location_table}
    location_name_to_area = {loc["name"]: loc["area"] for loc in location_table}

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = VacationSimOptions
    options: VacationSimOptions

    required_client_version = (0, 4, 4)

    def __init__(self, multiworld, player):
        super(VacationSimWorld, self).__init__(multiworld, player)

    def create_item(self, name: str) -> "VacationSimItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id - 1

        return VacationSimItem(name, item_table[id]["classification"], item_id, player=self.player)
    
    def get_filler_item_name(self) -> str:
        return "Positive Reinforcement"

    def create_items(self) -> None:
        for item in item_table:
            count = item["count"]
            
            if item["name"] == "Vacation Beach Gate Unlock" and self.options.starting_gate == 0:
                count = 0
                self.multiworld.push_precollected(self.create_item(item["name"]))
            elif item["name"] == "Vacation Forest Gate Unlock" and self.options.starting_gate == 1:
                count = 0
                self.multiworld.push_precollected(self.create_item(item["name"]))
            elif item["name"] == "Vacation Mountain Gate Unlock" and self.options.starting_gate == 2:
                count = 0
                self.multiworld.push_precollected(self.create_item(item["name"]))
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Vacation Island Resort", self.player, self.multiworld)
        beach_region = Region("Vacation Beach", self.player, self.multiworld)
        forest_region = Region("Vacation Forest", self.player, self.multiworld)
        mountain_region = Region("Vacation Mountain", self.player, self.multiworld)

        dive_site = Region("Dive Site", self.player, self.multiworld)
        hiking_trail = Region("Hiking Trail", self.player, self.multiworld)
        overlook = Region("Overlook", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            if self.location_name_to_area[loc] == "Vacation Island Resort":
                main_region.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], main_region))
            elif self.location_name_to_area[loc] == "Vacation Beach":
                beach_region.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], beach_region))
            elif self.location_name_to_area[loc] == "Vacation Forest":
                forest_region.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], forest_region))
            elif self.location_name_to_area[loc] == "Vacation Mountain":
                mountain_region.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], mountain_region))
            elif self.location_name_to_area[loc] == "Dive Site":
                dive_site.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], dive_site))
            elif self.location_name_to_area[loc] == "Hiking Trail":
                hiking_trail.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], hiking_trail))
            elif self.location_name_to_area[loc] == "Overlook":
                overlook.locations.append(VacationSimLocation(self.player, loc, self.location_name_to_id[loc], overlook))

        menu_region.connect(main_region)

        main_region.connect(beach_region, "Vacation Beach Main Gate", lambda state: state.has("Vacation Beach Gate Unlock", self.player))
        main_region.connect(forest_region, "Vacation Forest Main Gate", lambda state: state.has("Vacation Forest Gate Unlock", self.player))
        main_region.connect(mountain_region, "Vacation Mountain Main Gate", lambda state: state.has("Vacation Mountain Gate Unlock", self.player))

        beach_region.connect(main_region)
        forest_region.connect(main_region)
        mountain_region.connect(main_region)

        beach_region.connect(dive_site, "Boat to Dive Site", lambda state: state.has("Memory (Vacation Beach)", self.player, self.options.beach_memory_count))
        forest_region.connect(hiking_trail, "Hiking Trail Entrance", lambda state: state.has("Memory (Vacation Forest)", self.player, self.options.forest_memory_count))
        mountain_region.connect(overlook, "Gondola to Overlook", lambda state: state.has("Memory (Vacation Mountain)", self.player, self.options.mountain_memory_count))

        dive_site.connect(beach_region)
        hiking_trail.connect(forest_region)
        overlook.connect(mountain_region)

        self.multiworld.regions.append(main_region)
        self.multiworld.regions.append(beach_region)
        self.multiworld.regions.append(forest_region)
        self.multiworld.regions.append(mountain_region)

        self.multiworld.regions.append(dive_site)
        self.multiworld.regions.append(hiking_trail)
        self.multiworld.regions.append(overlook)

        self.multiworld.completion_condition[self.player] = lambda state: (state.has_group("Gates", self.player, 3)
            and state.has_group("Memories", self.player, self.options.final_memory_count)
            and state.can_reach(dive_site, self.player)
            and state.can_reach(hiking_trail, self.player)
            and state.can_reach(overlook, self.player))

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
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
                    "in_game_id": str(self.location_name_to_game_id[loc.name]),
                }

                locations[self.location_name_to_game_id[loc.name]] = data

        settings = {
            "beachGate": int(options.beach_memory_count),
            "forestGate": int(options.forest_memory_count),
            "mountainGate": int(options.mountain_memory_count),
            "finalGate": int(options.final_memory_count),
        }
    
        slot_data = {
            "locations": locations,
            "settings": settings,
        }
    
        return slot_data

class VacationSimItem(Item):
    game: str = "Vacation Simulator"

class VacationSimLocation(Location):
    game: str = "Vacation Simulator"