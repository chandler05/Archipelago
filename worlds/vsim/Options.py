from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class StartGate(Choice):
    """Determines which of the 3 areas will initially be open."""
    display_name = "Starting Area"
    option_vacation_beach = 0
    option_vacation_forest = 1
    option_vacation_mountain = 2
    default = "random"

class BeachMemories(Range):
    """The number of Vacation Beach Memories required to unlock the Dive Site."""
    display_name = "Vacation Beach Memory Requirement"
    range_start = 1
    range_end = 15
    default = 10

class ForestMemories(Range):
    """The number of Vacation Forest Memories required to unlock the Hiking Trail."""
    display_name = "Vacation Forest Memory Requirement"
    range_start = 1
    range_end = 15
    default = 10

class MountainMemories(Range):
    """The number of Vacation Mountain Memories required to unlock the Overlook."""
    display_name = "Vacation Mountain Memory Requirement"
    range_start = 1
    range_end = 15
    default = 10

class FinalMemories(Range):
    """The number of Vacation Memories required to flip the Party Switch."""
    display_name = "Party Switch Memory Requirement"
    range_start = 1
    range_end = 69
    default = 35

@dataclass
class VacationSimOptions(PerGameCommonOptions):
    starting_gate: StartGate
    beach_memory_count: BeachMemories
    forest_memory_count: ForestMemories
    mountain_memory_count: MountainMemories
    final_memory_count: FinalMemories