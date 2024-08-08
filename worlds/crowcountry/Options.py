from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class StartGate(Choice):
    """Determines which of the 3 areas will initially be open."""
    display_name = "Starting Area"
    option_vacation_beach = 0
    option_vacation_forest = 1
    option_vacation_mountain = 2
    default = "random"

@dataclass
class CrowCountryOptions(PerGameCommonOptions):
    starting_gate: StartGate