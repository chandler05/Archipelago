from collections import Counter
from typing import ClassVar, Dict, Any, Tuple, Type, List, Set
from BaseClasses import Region, Location, Item, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import ItemDict, get_item_table, group_table, base_id, get_all_items
from .Locations import location_table
from .Rules import create_rules
from .Options import CardSharkOptions

class CardSharkWeb(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Card Shark randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"]
    )]

class CardSharkWorld(World):
    """
    Card Shark is a card game about cheating at card games. Set in 18th century France,
    you must navigate political tensions and uncover a royal scandal by cheating your way
    through the upper echelon of French society.
    """

    game = "Card Shark"
    web = CardSharkWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in get_all_items()}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}
    item_name_to_classification = {item["name"]: item["classification"] for item in get_all_items()}

    early_placed_items = ["The Three Card Monte"]

    item_name_groups = group_table
    
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = CardSharkOptions
    options: CardSharkOptions

    required_client_version = (0, 4, 4)

    def get_filler_item_name(self) -> str:
        return "10 Livres"

    def create_item(self, name: str) -> "CardSharkItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id

        return CardSharkItem(name, self.item_name_to_classification[name], item_id, player=self.player)

    def create_items(self) -> None:
        self.full_item_table = get_item_table(self.options.split_tricks)
        
        self.multiworld.push_precollected(self.create_item("The Three Card Monte"))

        for item in self.full_item_table:
            count = item["count"]

            if item["name"] in self.early_placed_items:
                count = 0              

            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))

        junk = 0
        self.multiworld.itempool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Europe", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(CardSharkLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

        random_starter_trick = self.random.choice(self.get_first_items())

        if len(random_starter_trick) == 2:
            first = self.random.choice(["Cascarot Camp - Trick the Magician", "The Barn - Scenario 1"])
            second = "The Barn - Scenario 1" if first == "Cascarot Camp - Trick the Magician" else "Cascarot Camp - Trick the Magician"

            item_one = self.create_item(random_starter_trick[0])
            item_two = self.create_item(random_starter_trick[1])

            self.multiworld.get_location(first, self.player).place_locked_item(item_one)
            self.multiworld.get_location(second, self.player).place_locked_item(item_two)

            self.early_placed_items.append(random_starter_trick[0])
            self.early_placed_items.append(random_starter_trick[1])
        else:
            item = self.create_item(random_starter_trick)
            self.multiworld.get_location("Cascarot Camp - Trick the Magician", self.player).place_locked_item(item)

            self.early_placed_items.append(random_starter_trick)

        if self.options.goal == "complete_all_scenarios":
            if self.options.split_tricks:
                self.multiworld.completion_condition[self.player] = lambda state: (state.has_all(self.item_name_groups['split_card_tricks'], self.player)
                    and state.has("The Three Card Monte", self.player))
            else:
                self.multiworld.completion_condition[self.player] = lambda state: (state.has_all(self.item_name_groups['card_tricks'], self.player)
                    and state.has("The Three Card Monte", self.player))
        if self.options.goal == "complete_final_scenario":
            if self.options.split_tricks:
                self.multiworld.completion_condition[self.player] = lambda state: (state.has("Palm Glimpse", self.player) and state.has("Second Deal", self.player)
                    and state.has("Shark Deal", self.player) and state.has("Sticky Hand", self.player) and state.has("Full Harvest", self.player)
                    and state.has("Erdnase Shuffle", self.player) and state.has("Blank Cut", self.player) and state.has("Bottom Drag", self.player)
                    and state.has("False Riffle Shuffle", self.player))
            else:
                self.multiworld.completion_condition[self.player] = lambda state: (state.has("The Comte's Gambit", self.player)
                    and state.has("The Erdnase Stack", self.player) and state.has("The Expert Dealer", self.player))

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options

        settings = {
            "goal": int(options.goal),
            "splitTricks": int(options.split_tricks),
        }
    
        slot_data = {
            "settings": settings,
        }
    
        return slot_data
    
    def get_first_items(self) -> List[List[str]]:
        output: Set[List[str]] = set()
        if self.options.split_tricks:
            output = {("Top Drag", "Ineffective Shuffle"), ("Sticky Hand", "Single Card Shuffle"),
                      ("Wine Glimpse", "Wipe Signal"), ("Full Harvest", "Ineffective Shuffle"),
                      ("Dealer's Glimpse", "Pinch and Drop Signal"), ("Crooked Card", "Single Card Shuffle")}
        else:
            output = {("The Bottle of Cahors"),  ("The Dishevelled Gatherer"), ("The Indiscreet Fingers"),
                      ("The Stolen Card"), ("The Bent Card"), ("The Beginner Stack")}

        return list(output)

class CardSharkItem(Item):
    game: str = "Card Shark"

class CardSharkLocation(Location):
    game: str = "Card Shark"
