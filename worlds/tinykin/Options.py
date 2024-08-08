from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, StartInventoryPool

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
    Each type of Tinykin can have an item unlock them for all areas (global), or for each area individually."""
    display_name = "Unlock Tinykin"
    option_off = 0
    option_global = 1
    option_per_area = 2
    default = 1

class SoapboardLogic(Toggle):
    """When enabled, the Soapboard will be placed into the item pool. Otherwise, you will receive it towards the beginning of the game."""
    display_name = "Soapboard Logic"

class AreaShuffle(Toggle):
    """Shuffles the order of the areas in the game."""
    display_name = "Area Shuffle"

class RaceTier(Choice):
    """The highest tier in the race challenges that will have a location check."""
    display_name = "Highest Race Tier"
    option_disabled = 0
    option_bronze = 1
    option_silver = 2
    option_gold = 3
    option_platinum = 4
    default = 3

@dataclass
class TinykinOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    tinykin_unlocks: TinykinUnlocks
    soapboard_logic: SoapboardLogic
    area_shuffle: AreaShuffle
    race_tier: RaceTier