from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from worlds.zackandwiki.names import Regions

if TYPE_CHECKING:
    from .world import ZackAndWikiWorld

def create_and_connect_regions(world: ZackAndWikiWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: ZackAndWikiWorld) -> None:
    menu = Region(Regions.MENU, world.player, world.multiworld)
    jungle_ruins = Region(Regions.JUNGLE_RUINS, world.player, world.multiworld)
    a_journey_begins = Region(Regions.A_JOURNEY_BEGINS, world.player, world.multiworld)
    pit_of_tragedy = Region(Regions.PIT_OF_TRAGEDY, world.player, world.multiworld)
    flute_of_the_goblins = Region(Regions.FLUTE_OF_THE_GOBLINS, world.player, world.multiworld)

    regions = [menu, jungle_ruins, a_journey_begins, pit_of_tragedy, flute_of_the_goblins]

    world.multiworld.regions += regions


def connect_regions(world: ZackAndWikiWorld) -> None:
    menu = world.get_region(Regions.MENU)
    jungle_ruins = world.get_region(Regions.JUNGLE_RUINS)
    a_journey_begins = world.get_region(Regions.A_JOURNEY_BEGINS)
    pit_of_tragedy = world.get_region(Regions.PIT_OF_TRAGEDY)
    flute_of_the_goblins = world.get_region(Regions.FLUTE_OF_THE_GOBLINS)

    menu.connect(jungle_ruins, f"{Regions.MENU} to {Regions.JUNGLE_RUINS}")
    jungle_ruins.connect(a_journey_begins, f"{Regions.JUNGLE_RUINS} to {Regions.A_JOURNEY_BEGINS}")
    jungle_ruins.connect(pit_of_tragedy, f"{Regions.JUNGLE_RUINS} to {Regions.PIT_OF_TRAGEDY}")
    jungle_ruins.connect(flute_of_the_goblins, f"{Regions.JUNGLE_RUINS} to {Regions.FLUTE_OF_THE_GOBLINS}")