from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import ZackAndWikiWorld

def set_all_rules(world: ZackAndWikiWorld) -> None:
    return
    #set_all_entrance_rules(world)
    #set_all_location_rules(world)
    #set_completion_condition(world)


#def set_all_entrance_rules(world: APQuestWorld) -> None:

#def set_all_location_rules(world: APQuestWorld) -> None:

#def set_completion_condition(world: APQuestWorld) -> None: