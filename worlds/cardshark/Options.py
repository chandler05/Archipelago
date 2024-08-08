from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, StartInventoryPool, Toggle

class Goal(Choice):
    """Choose the end goal.
    Complete All Scenarios: Collect all necessary tricks and complete all scenarios to reach the goal.
    Complete Final Scenario: Only complete the final scenario (Versailles) to reach the goal."""
    display_name = "Goal"
    option_complete_all_scenarios = 0
    option_complete_final_scenario = 1
    default = 0

class SplitTricks(Toggle):
    """When enabled, card tricks will be split into their pieces and placed into the item pool.
    All of the pieces of a trick must be collected to perform it."""
    display_name = "Split Card Tricks"

@dataclass
class CardSharkOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    split_tricks: SplitTricks
