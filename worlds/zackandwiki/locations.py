from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items
from worlds.zackandwiki.names import Game as G, Locations as L, Regions as R

if TYPE_CHECKING:
    from .world import ZackAndWikiWorld

LOCATION_NAME_TO_ID = {
    L.A_JOURNEY_BEGINS_TREASURE: 110,
    L.A_JOURNEY_BEGINS_MYSTERIOUS_TREASURE: 111,
    L.PIT_OF_TRAGEDY_TREASURE: 120,
    L.PIT_OF_TRAGEDY_MYSTERIOUS_TREASURE: 121,
    L.PIT_OF_TRAGEDY_SECRET_CHEST_1: 122,
    L.PIT_OF_TRAGEDY_SECRET_CHEST_2: 123,
    L.FLUTE_OF_THE_GOBLINS_TREASURE: 130,
    L.FLUTE_OF_THE_GOBLINS_MYSTERIOUS_TREASURE: 131,
    L.FLUTE_OF_THE_GOBLINS_BONELICH: 132,
    L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_1: 133,
    L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_2: 134,
    L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_3: 135,
}

class ZackAndWikiLocation(Location):
    game = G.GAME

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: ZackAndWikiWorld) -> None:
    create_regular_locations(world)
    #create_events(world)

def create_regular_locations(world: ZackAndWikiWorld) -> None:
    a_journey_begins = world.get_region(R.A_JOURNEY_BEGINS)
    pit_of_tragedy = world.get_region(R.PIT_OF_TRAGEDY)
    flute_of_the_goblins = world.get_region(R.FLUTE_OF_THE_GOBLINS)

    a_journey_begins.add_locations(get_location_names_with_ids(
        [
            L.A_JOURNEY_BEGINS_TREASURE,
            L.A_JOURNEY_BEGINS_MYSTERIOUS_TREASURE
        ]
    ), ZackAndWikiLocation)
    pit_of_tragedy.add_locations(get_location_names_with_ids(
        [
            L.PIT_OF_TRAGEDY_TREASURE,
            L.PIT_OF_TRAGEDY_MYSTERIOUS_TREASURE,
            L.PIT_OF_TRAGEDY_SECRET_CHEST_1,
            L.PIT_OF_TRAGEDY_SECRET_CHEST_2
        ]
    ), ZackAndWikiLocation)
    flute_of_the_goblins.add_locations(get_location_names_with_ids(
        [
            L.FLUTE_OF_THE_GOBLINS_TREASURE,
            L.FLUTE_OF_THE_GOBLINS_MYSTERIOUS_TREASURE,
            L.FLUTE_OF_THE_GOBLINS_BONELICH,
            L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_1,
            L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_2,
            L.FLUTE_OF_THE_GOBLINS_SECRET_CHEST_3
        ]
    ), ZackAndWikiLocation)

#def create_events(world: ZackAndWikiLocation) -> None: