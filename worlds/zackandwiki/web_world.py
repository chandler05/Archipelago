from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups
from worlds.zackandwiki.names import Game


class ZackAndWikiWebWorld(WebWorld):
    game = Game.GAME
    theme = "ocean"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Zack & Wiki: Quest for Barbaros' Treasure for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chandler"],
    )
    tutorials = [setup_en]

    option_groups = option_groups