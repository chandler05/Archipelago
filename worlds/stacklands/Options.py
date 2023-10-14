from typing import Dict
from Options import AssembleOptions, Choice, Range, Toggle

class Goal(Choice):
    """Choose the end goal.
    Kill the Demon Lord"""
    display_name = "Goal"
    option_kill_the_demon_lord = 0
    default = 0

stacklands_options: Dict[str, AssembleOptions] = {
    "goal": Goal
}