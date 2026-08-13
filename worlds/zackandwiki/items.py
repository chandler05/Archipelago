from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification
from .names import Items, Game

if TYPE_CHECKING:
    from .world import ZackAndWikiWorld

@dataclass
class ItemData:
    id: int
    classification: ItemClassification = ItemClassification.progression
    amount: int = 1

item_table: Dict[str, ItemData] = {
    Items.CENTIPEDE: ItemData(id = 1),
    Items.SNAKE: ItemData(id = 2),
    Items.FROG: ItemData(id = 3),
    Items.BAT: ItemData(id = 4),
    Items.WORM: ItemData(id = 5, classification = ItemClassification.filler),
    Items.GOBLIN: ItemData(id = 6),
    Items.KING_GROWL: ItemData(id = 7),
    Items.ZENNY: ItemData(id = 8, classification = ItemClassification.filler, amount = 0),
    Items.PLATINUM_TICKET: ItemData(id = 9, classification = ItemClassification.filler, amount = 0),
    Items.ORACLE_DOLL: ItemData(id = 10, classification = ItemClassification.filler, amount = 0),
}

ITEM_NAME_TO_ID = {key: value.id for key, value in item_table.items()}

class ZackAndWikiItem(Item):
    game = Game.GAME

def get_random_filler_item_name(world: ZackAndWikiWorld) -> str:
    filler_items = [Items.ZENNY, Items.PLATINUM_TICKET, Items.ORACLE_DOLL]
    return filler_items[world.random.randrange(0, len(filler_items))]

def create_item_with_correct_classification(world: ZackAndWikiWorld, name: str) -> ZackAndWikiItem:
    return ZackAndWikiItem(name, item_table[name].classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: ZackAndWikiWorld) -> None:
    itempool: list[Item] = []

    for item in item_table.keys():
        for n in range(item_table[item].amount):
            itempool.append(world.create_item(item))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool