from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, StartInventoryPool, Toggle

class Goal(Choice):
    """Choose the end goal."""
    display_name = "Goal"
    option_defeat_agent_rainbow = 0
    default = 0

class Healthsanity(Toggle):
    """When enabled, health pickups will be replaced with location checks and added to the item pool."""
    display_name = "Healthsanity"

class EnemyDropChecks(Toggle):
    """When enabled, enemies with item drops will have their drops replaced with location checks."""
    display_name = "Enemy Drop Checks"

@dataclass
class InSoundMindOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    healthsanity: Healthsanity
    enemy_drop_checks: EnemyDropChecks
