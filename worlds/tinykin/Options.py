from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class Goal(Choice):
    """Choose the end goal.
    Find Ardwen: Vanilla ending. Find Ardwen in the final room.
    All Pollen: Collect all of the pollen for each area in the game."""
    display_name = "Goal"
    option_find_ardwen = 0
    option_all_pollen = 1
    default = 0

class TinykinUnlocks(Choice):
    """When enabled, each type of Tinykin will be locked behind an item placed into the item pool.
    Each type of Tinykin can have an item unlock them for all areas, or for each area individually."""
    display_name = "Unlock Tinykin"
    option_off = 0
    option_global = 1
    option_per_area = 2
    default = 1

class SoapboardLogic(DefaultOnToggle):
    """When enabled, the Soapboard will be placed into the item pool. Otherwise, you will receive it towards the beginning of the game."""
    display_name = "Soapboard Logic"

class AreaShuffle(DefaultOnToggle):
    """Shuffles the order of the areas in the game."""
    display_name = "Area Shuffle"

class RaceTier(Choice):
    """The highest tier in the race challenges that will have a location check."""
    display_name = "Highest Race Tier"
    option_platinum = 0
    option_gold = 1
    default = 0

@dataclass
class TinykinOptions(PerGameCommonOptions):
    goal: Goal
    tinykin_unlocks: TinykinUnlocks
    soapboard_logic: SoapboardLogic
    area_shuffle: AreaShuffle
    race_tier: RaceTier