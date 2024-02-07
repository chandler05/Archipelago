from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle

class Goal(Choice):
    """Choose the end goal.
    One Crown: Complete one run and obtain a single crown.
    Three Crowns: Complete three runs in a row without taking damage and obtain three crown."""
    display_name = "Goal"
    option_one_crown = 0
    option_three_crowns = 1
    default = 1

@dataclass
class PizzaPossumOptions(PerGameCommonOptions):
    goal: Goal