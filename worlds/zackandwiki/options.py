from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, DefaultOnToggle

class BarbarosParts(Choice):
    """
    Controls whether or not Barbaros' Body Parts will be shuffled
    into the item pool or remain in their vanilla locations.
    """

    display_name = "Barbaros' Body Parts"

    option_vanilla = 0
    option_shuffled = 1

    default = option_vanilla

class BonelichChecks(DefaultOnToggle):
    """
    Controls whether or not Bonelich's music challenges
    will be locations in the world.
    """

    display_name = "Bonelich Checks"

class LevelOrder(Choice):
    """
    Controls the order of the levels in the game.
    Local Shuffle keeps them in their worlds.
    Global Shuffle puts them anywhere in the game.
    (This doesn't apply to the final two levels)
    """

    display_name = "Level Order"

    option_vanilla = 0
    option_local_shuffle = 1
    option_global_shuffle = 2

    default = option_vanilla

class IndividualTotems(DefaultOnToggle):
    """
    Controls whether or not the totem items will be separated
    by type or placed in a single general totem item.
    """

    display_name = "Individual Totem Items"

@dataclass
class ZackAndWikiOptions(PerGameCommonOptions):
    barbaros_parts: BarbarosParts
    bonelich_checks: BonelichChecks
    level_order: LevelOrder
    individual_totems: IndividualTotems

option_groups = [
    OptionGroup(
        "General Options",
        [LevelOrder],
    ),
    OptionGroup(
        "Location Options",
        [BonelichChecks],
    ),
    OptionGroup(
        "Item Options",
        [BarbarosParts, IndividualTotems],
    ),
]